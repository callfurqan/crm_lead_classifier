from dataclasses import dataclass, field

from src.models.classification import Classification
from src.models.extracted_info import ExtractedInfo
from src.models.enums import DatasetType
from src.models.interaction import Interaction


@dataclass
class Lead:
    """
    Normalized CRM Lead.
    Every processor returns Lead objects.
    """

    lead_id: str

    lead_key: str

    name: str = ""

    email: str = ""

    phone: str = ""

    company: str = ""

    assigned_to: str = ""

    datasets: set[DatasetType] = field(default_factory=set)

    interactions: list[Interaction] = field(default_factory=list)

    extracted: ExtractedInfo = field(default_factory=ExtractedInfo)

    classification: Classification = field(default_factory=Classification)

    metadata: dict = field(default_factory=dict)