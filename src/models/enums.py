from enum import Enum


class DatasetType(str, Enum):
    EMAIL = "email"
    SMS = "sms"
    CALL = "call"


class InteractionDirection(str, Enum):
    INBOUND = "inbound"
    OUTBOUND = "outbound"


class ClassificationStatus(str, Enum):
    INTERESTED = "interested"
    NON_INTERESTED = "non_interested"
    UNKNOWN = "unknown"


class InterestLevel(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    UNKNOWN = "unknown"