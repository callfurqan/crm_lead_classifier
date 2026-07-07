from dataclasses import dataclass, field

from .interaction import Interaction
from .classification import Classification
from .extracted_info import ExtractedInfo

from .enums import DatasetType


@dataclass
class Lead:

    lead_id: str

    dataset: DatasetType

    name: str = ""

    email: str = ""

    phone: str = ""

    company: str = ""

    assigned_to: str = ""

    interactions: list[Interaction] = field(default_factory=list)

    extracted: ExtractedInfo = field(default_factory=ExtractedInfo)

    classification: Classification = field(default_factory=Classification)

    metadata: dict = field(default_factory=dict)