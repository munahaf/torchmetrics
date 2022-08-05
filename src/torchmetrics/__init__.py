r"""Root package info."""
import logging as __logging
import os

from torchmetrics.__about__ import *  # noqa: F401, F403

_logger = __logging.getLogger("torchmetrics")
_logger.addHandler(__logging.StreamHandler())
_logger.setLevel(__logging.INFO)

_PACKAGE_ROOT = os.path.dirname(__file__)
_PROJECT_ROOT = os.path.dirname(_PACKAGE_ROOT)

from torchmetrics import functional  # noqa: E402
from torchmetrics.aggregation import CatMetric, MaxMetric, MeanMetric, MinMetric, SumMetric  # noqa: E402
from torchmetrics.audio import (  # noqa: E402
    PermutationInvariantTraining,
    ScaleInvariantSignalDistortionRatio,
    ScaleInvariantSignalNoiseRatio,
    SignalDistortionRatio,
    SignalNoiseRatio,
)
from torchmetrics.classification import (  # noqa: E402
    AUC,
    AUROC,
    ROC,
    Accuracy,
    AveragePrecision,
    BinaryAccuracy,
    BinaryCohenKappa,
    BinaryConfusionMatrix,
    BinaryF1Score,
    BinaryFBetaScore,
    BinaryHammingDistance,
    BinaryJaccardIndex,
    BinaryMatthewsCorrCoef,
    BinaryPrecision,
    BinaryRecall,
    BinarySpecificity,
    BinaryStatScores,
    BinnedAveragePrecision,
    BinnedPrecisionRecallCurve,
    BinnedRecallAtFixedPrecision,
    CalibrationError,
    CohenKappa,
    ConfusionMatrix,
    CoverageError,
    Dice,
    F1Score,
    FBetaScore,
    HammingDistance,
    HingeLoss,
    JaccardIndex,
    KLDivergence,
    LabelRankingAveragePrecision,
    LabelRankingLoss,
    MatthewsCorrCoef,
    MulticlassAccuracy,
    MulticlassCohenKappa,
    MulticlassConfusionMatrix,
    MulticlassF1Score,
    MulticlassFBetaScore,
    MulticlassHammingDistance,
    MulticlassJaccardIndex,
    MulticlassMatthewsCorrCoef,
    MulticlassPrecision,
    MulticlassRecall,
    MulticlassSpecificity,
    MulticlassStatScores,
    MultilabelAccuracy,
    MultilabelConfusionMatrix,
    MultilabelExactMatch,
    MultilabelF1Score,
    MultilabelFBetaScore,
    MultilabelHammingDistance,
    MultilabelJaccardIndex,
    MultilabelMatthewsCorrCoef,
    MultilabelPrecision,
    MultilabelRecall,
    MultilabelSpecificity,
    MultilabelStatScores,
    Precision,
    PrecisionRecallCurve,
    Recall,
    Specificity,
    StatScores,
)
from torchmetrics.collections import MetricCollection  # noqa: E402
from torchmetrics.image import (  # noqa: E402
    ErrorRelativeGlobalDimensionlessSynthesis,
    MultiScaleStructuralSimilarityIndexMeasure,
    PeakSignalNoiseRatio,
    SpectralAngleMapper,
    SpectralDistortionIndex,
    StructuralSimilarityIndexMeasure,
    UniversalImageQualityIndex,
)
from torchmetrics.metric import Metric  # noqa: E402
from torchmetrics.regression import (  # noqa: E402
    CosineSimilarity,
    ExplainedVariance,
    MeanAbsoluteError,
    MeanAbsolutePercentageError,
    MeanSquaredError,
    MeanSquaredLogError,
    PearsonCorrCoef,
    R2Score,
    SpearmanCorrCoef,
    SymmetricMeanAbsolutePercentageError,
    TweedieDevianceScore,
    WeightedMeanAbsolutePercentageError,
)
from torchmetrics.retrieval import (  # noqa: E402
    RetrievalFallOut,
    RetrievalHitRate,
    RetrievalMAP,
    RetrievalMRR,
    RetrievalNormalizedDCG,
    RetrievalPrecision,
    RetrievalPrecisionRecallCurve,
    RetrievalRecall,
    RetrievalRecallAtFixedPrecision,
    RetrievalRPrecision,
)
from torchmetrics.text import (  # noqa: E402
    BLEUScore,
    CharErrorRate,
    CHRFScore,
    ExtendedEditDistance,
    MatchErrorRate,
    Perplexity,
    SacreBLEUScore,
    SQuAD,
    TranslationEditRate,
    WordErrorRate,
    WordInfoLost,
    WordInfoPreserved,
)
from torchmetrics.wrappers import (  # noqa: E402
    BootStrapper,
    ClasswiseWrapper,
    MetricTracker,
    MinMaxMetric,
    MultioutputWrapper,
)

__all__ = [
    "functional",
    "Accuracy",
    "BinaryAccuracy",
    "MulticlassAccuracy",
    "MultilabelAccuracy",
    "AUC",
    "AUROC",
    "AveragePrecision",
    "BinnedAveragePrecision",
    "BinnedPrecisionRecallCurve",
    "BinnedRecallAtFixedPrecision",
    "BLEUScore",
    "BootStrapper",
    "CalibrationError",
    "CatMetric",
    "ClasswiseWrapper",
    "CharErrorRate",
    "CHRFScore",
    "CohenKappa",
    "BinaryCohenKappa",
    "MulticlassCohenKappa",
    "ConfusionMatrix",
    "BinaryConfusionMatrix",
    "MulticlassConfusionMatrix",
    "MultilabelConfusionMatrix",
    "CosineSimilarity",
    "CoverageError",
    "Dice",
    "TweedieDevianceScore",
    "ErrorRelativeGlobalDimensionlessSynthesis",
    "ExplainedVariance",
    "ExtendedEditDistance",
    "F1Score",
    "BinaryF1Score",
    "MulticlassF1Score",
    "MultilabelF1Score",
    "FBetaScore",
    "BinaryFBetaScore",
    "MulticlassFBetaScore",
    "MultilabelFBetaScore",
    "HammingDistance",
    "BinaryHammingDistance",
    "MultilabelHammingDistance",
    "MulticlassHammingDistance",
    "HingeLoss",
    "JaccardIndex",
    "BinaryJaccardIndex",
    "MulticlassJaccardIndex",
    "MultilabelJaccardIndex",
    "MultilabelExactMatch",
    "KLDivergence",
    "LabelRankingAveragePrecision",
    "LabelRankingLoss",
    "MatchErrorRate",
    "MatthewsCorrCoef",
    "BinaryMatthewsCorrCoef",
    "MulticlassMatthewsCorrCoef",
    "MultilabelMatthewsCorrCoef",
    "MaxMetric",
    "MeanAbsoluteError",
    "MeanAbsolutePercentageError",
    "MeanMetric",
    "MeanSquaredError",
    "MeanSquaredLogError",
    "Metric",
    "MetricCollection",
    "MetricTracker",
    "MinMaxMetric",
    "MinMetric",
    "MultioutputWrapper",
    "MultiScaleStructuralSimilarityIndexMeasure",
    "PearsonCorrCoef",
    "PermutationInvariantTraining",
    "Perplexity",
    "Precision",
    "BinaryPrecision",
    "MulticlassPrecision",
    "MultilabelPrecision",
    "PrecisionRecallCurve",
    "PeakSignalNoiseRatio",
    "R2Score",
    "Recall",
    "BinaryRecall",
    "MulticlassRecall",
    "MultilabelRecall",
    "RetrievalFallOut",
    "RetrievalHitRate",
    "RetrievalMAP",
    "RetrievalMRR",
    "RetrievalNormalizedDCG",
    "RetrievalPrecision",
    "RetrievalRecall",
    "RetrievalRPrecision",
    "RetrievalPrecisionRecallCurve",
    "RetrievalRecallAtFixedPrecision",
    "ROC",
    "SacreBLEUScore",
    "SignalDistortionRatio",
    "ScaleInvariantSignalDistortionRatio",
    "ScaleInvariantSignalNoiseRatio",
    "SignalNoiseRatio",
    "SpearmanCorrCoef",
    "Specificity",
    "BinarySpecificity",
    "MulticlassSpecificity",
    "MultilabelSpecificity",
    "SpectralAngleMapper",
    "SpectralDistortionIndex",
    "SQuAD",
    "StructuralSimilarityIndexMeasure",
    "StatScores",
    "BinaryStatScores",
    "MulticlassStatScores",
    "MultilabelStatScores",
    "SumMetric",
    "SymmetricMeanAbsolutePercentageError",
    "TranslationEditRate",
    "UniversalImageQualityIndex",
    "WeightedMeanAbsolutePercentageError",
    "WordErrorRate",
    "WordInfoLost",
    "WordInfoPreserved",
]
