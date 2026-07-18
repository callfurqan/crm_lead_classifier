from enum import Enum


class DatasetType(Enum):
    EMAIL = "email"
    SMS = "sms"
    CALL = "call"


class InteractionDirection(Enum):
    INBOUND = "inbound"
    OUTBOUND = "outbound"


class InteractionSource(Enum):
    SMS = "sms"
    EMAIL = "email"
    CALL = "call"


class ClassificationStatus(Enum):
    UNKNOWN = "unknown"
    INTERESTED = "interested"
    NON_INTERESTED = "non_interested"


class InterestLevel(Enum):
    UNKNOWN = "unknown"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"