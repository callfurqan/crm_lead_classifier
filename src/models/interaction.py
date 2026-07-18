from dataclasses import dataclass, field
from datetime import datetime

from src.models.enums import (
    InteractionDirection,
    InteractionSource,
)


@dataclass
class Interaction:
    """
    Represents one communication event.
    """

    source: InteractionSource

    direction: InteractionDirection

    timestamp: datetime | None = None

    sender: str = ""

    receiver: str = ""

    content: str = ""

    metadata: dict = field(default_factory=dict)