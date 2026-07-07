from src.models.enums import DatasetType

from .email_processor import EmailProcessor
from .sms_processor import SMSProcessor
from .call_processor import CallProcessor


PROCESSOR_REGISTRY = {
    DatasetType.EMAIL: EmailProcessor,
    DatasetType.SMS: SMSProcessor,
    DatasetType.CALL: CallProcessor,
}