from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any

from .enums import InteractionDirection


@dataclass
class Interaction:

    source: str

    direction: InteractionDirection

    timestamp: datetime | None

    sender: str

    receiver: str

    content: str

    metadata: Dict[str, Any] = field(default_factory=dict)