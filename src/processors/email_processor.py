from src.models.lead import Lead
from .base_processor import BaseProcessor


class EmailProcessor(BaseProcessor):

    def process(self, data: dict) -> list[Lead]:
        """
        Email parsing will be implemented in Sprint 4.
        """

        leads: list[Lead] = []

        return leads