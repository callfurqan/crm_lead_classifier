from abc import ABC, abstractmethod

from src.models.lead import Lead

from src.builders.lead_builder import LeadBuilder
from src.builders.interaction_builder import InteractionBuilder
from src.core.processor_result import ProcessorResult


class BaseProcessor(ABC):

    def build_lead(self, **kwargs):
        return LeadBuilder.create(**kwargs)

    def build_interaction(self, **kwargs):
        return InteractionBuilder.create(**kwargs)

    @abstractmethod
    def process(self, data: dict) -> ProcessorResult:
        pass