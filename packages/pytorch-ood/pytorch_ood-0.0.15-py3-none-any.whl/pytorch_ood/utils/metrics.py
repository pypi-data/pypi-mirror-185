"""
..  autoclass:: pytorch_ood.utils.OODMetrics
    :members:

"""
import numpy as np
import torch
import torchmetrics

from .utils import TensorBuffer, is_unknown


def calibration_error(
    confidence: torch.Tensor, correct: torch.Tensor, p: str = "2", beta: int = 100
) -> float:
    """
    :see Implementation: `GitHub <https://github.com/hendrycks/natural-adv-examples/>`__

    :param confidence: predicted confidence
    :param correct: ground truth
    :param p: p for norm. Can be one of ``1``, ``2``, or ``infty``
    :param beta: target bin size
    :return: calculated calibration error
    """

    confidence = confidence.numpy()
    correct = correct.numpy()

    idxs = np.argsort(confidence)
    confidence = confidence[idxs]
    correct = correct[idxs]
    bins = [[i * beta, (i + 1) * beta] for i in range(len(confidence) // beta)]
    bins[-1] = [bins[-1][0], len(confidence)]

    cerr = 0
    total_examples = len(confidence)
    for i in range(len(bins) - 1):
        bin_confidence = confidence[bins[i][0] : bins[i][1]]
        bin_correct = correct[bins[i][0] : bins[i][1]]
        num_examples_in_bin = len(bin_confidence)

        if num_examples_in_bin > 0:
            difference = np.abs(np.nanmean(bin_confidence) - np.nanmean(bin_correct))

            if p == "2":
                cerr += num_examples_in_bin / total_examples * np.square(difference)
            elif p == "1":
                cerr += num_examples_in_bin / total_examples * difference
            elif p == "infty" or p == "infinity" or p == "max":
                cerr = np.maximum(cerr, difference)
            else:
                assert False, "p must be '1', '2', or 'infty'"

    if p == "2":
        cerr = np.sqrt(cerr)

    return float(cerr)


def aurra(confidence: torch.Tensor, correct: torch.Tensor) -> float:
    """
    :see Implementation: `GitHub <https://github.com/hendrycks/natural-adv-examples/>`__

    :param confidence: predicted confidence values
    :param correct: ground truth

    :return: score
    """
    conf_ranks = np.argsort(confidence.numpy())[::-1]  # indices from greatest to least confidence
    rra_curve = np.cumsum(np.asarray(correct.numpy())[conf_ranks])
    rra_curve = rra_curve / np.arange(1, len(rra_curve) + 1)  # accuracy at each response rate
    return float(np.mean(rra_curve))


def fpr_at_tpr(pred, target, k=0.95):
    """
    Calculate the False Positive Rate at a certain True Positive Rate

    TODO: use bisect

    :param pred: outlier scores
    :param target: target label
    :param k: cutoff value
    :return:
    """
    fpr, tpr, thresholds = torchmetrics.functional.roc(pred, target)
    for fp, tp, t in zip(fpr, tpr, thresholds):
        if tp >= k:
            return fp

    return torch.tensor(1.0)


def accuracy_at_tpr(pred, target, k=0.95):
    """
    Calculate the accurcy at a certain True Positive Rate

    TODO: use bisect

    :param pred: outlier scores
    :param target: target label
    :param k: cutoff value
    :return:
    """
    fpr, tpr, thresholds = torchmetrics.functional.roc(pred, target)
    for fp, tp, t in zip(fpr, tpr, thresholds):
        if tp >= k:
            labels = torch.where(pred >= t, 1, 0)
            return torchmetrics.functional.accuracy(labels, target)

    return torch.tensor(0.0)


class OODMetrics(object):
    """
    Calculates various metrics used in OOD detection experiments.

    - AUROC
    - AUPR IN/OUT
    - FPR\\@95TPR
    - ACC\\@95TPR

    The interface is similar to ``torchmetrics``.

    .. code :: python

        metrics = OODMetrics()
        outlier_scores = torch.Tensor([0.5, 1.0, -10])
        labels = torch.Tensor([1,2,-1])
        metrics.update(outlier_scores, labels)
        metric_dict = metrics.compute()

    .. warning :: This implementation is not optimized and might consume large amounts of memory.

    """

    def __init__(self, device="cpu"):
        """
        :param device: where tensors should be stored
        """
        super(OODMetrics, self).__init__()
        self.device = device
        self.buffer = TensorBuffer(device=self.device)
        self.auroc = torchmetrics.classification.BinaryAUROC(num_classes=2)
        self.aupr_in = torchmetrics.classification.BinaryPrecisionRecallCurve(pos_label=1)
        self.aupr_out = torchmetrics.classification.BinaryPrecisionRecallCurve(pos_label=0)

    def update(self, outlier_scores: torch.Tensor, y: torch.Tensor) -> None:
        """
        Add batch of results to collection.

        :param outlier_scores: outlier score
        :param y: target label
        """
        label = is_unknown(y).detach().to(self.device).long()
        o = outlier_scores.detach().to(self.device)

        self.auroc.update(o, label)
        self.aupr_in.update(o, label)
        self.aupr_out.update(-o, 1 - label)
        self.buffer.append("scores", outlier_scores)
        self.buffer.append("labels", label)

    def compute(self) -> dict:
        """
        Calculate metrics

        :return: dictionary with different metrics
        :raise: ValueError if data does not contain IN and OOD points or buffer is empty
        """
        if self.buffer.is_empty():
            raise ValueError("Must be given data to calculate metrics.")

        labels = self.buffer.get("labels")
        scores = self.buffer.get("scores")

        if len(torch.unique(labels)) != 2:
            raise ValueError("Data must contain IN and OOD samples.")

        auroc = self.auroc.compute()

        p, r, t = self.aupr_in.compute()
        aupr_in = torchmetrics.functional.auc(r, p, reorder=True)

        p, r, t = self.aupr_out.compute()
        aupr_out = torchmetrics.functional.auc(r, p)

        acc = accuracy_at_tpr(scores, labels)
        fpr = fpr_at_tpr(scores, labels)

        return {
            "AUROC": auroc.item(),
            "AUPR-IN": aupr_in.item(),
            "AUPR-OUT": aupr_out.item(),
            "ACC95TPR": acc.item(),
            "FPR95TPR": fpr.item(),
        }

    def reset(self) -> None:
        """
        Resets collected metrics
        """
        self.auroc.reset()
        self.aupr_in.reset()
        self.aupr_out.reset()
        self.buffer.clear()


class ErrorDetectionMetrics(object):
    def __init__(self):
        self.buffer = TensorBuffer()

    def update(self, outlier_scores, y, y_hat) -> None:
        """

        :param outlier_scores: outlier score
        :param y: true label
        :param y_hat: predicted label
        """
        self.buffer.append("scores", outlier_scores)
        self.buffer.append("y", y)
        self.buffer.append("y_hat", y_hat)

    def compute(self) -> dict:
        y = self.buffer.get("y")
        s = self.buffer.get("scores")
        y_hat = self.buffer.get("y_hat")

        correct = y_hat.eq(y)
