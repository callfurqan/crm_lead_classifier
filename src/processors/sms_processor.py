from src.models.lead import Lead
from .base_processor import BaseProcessor


class SMSProcessor(BaseProcessor):

    def process(self, data: dict) -> list[Lead]:
        """
        SMS parsing will be implemented in Sprint 4.
        """

        leads: list[Lead] = []

        return leads