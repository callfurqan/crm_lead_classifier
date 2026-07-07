from dataclasses import dataclass, field

from .enums import ClassificationStatus
from .enums import InterestLevel


@dataclass
class Classification:

    status: ClassificationStatus = ClassificationStatus.UNKNOWN

    level: InterestLevel = InterestLevel.UNKNOWN

    confidence: float = 0.0

    reason: str = ""

    classifier: str = "rule"

    tags: list[str] = field(default_factory=list)