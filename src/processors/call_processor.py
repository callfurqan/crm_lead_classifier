from src.models.lead import Lead
from .base_processor import BaseProcessor
from src.core.processor_result import ProcessorResult
from src.core.parser_statistics import ParserStatistics

class CallProcessor(BaseProcessor):

    def process(self, data: dict) -> list[Lead]:
        """
        Call parsing will be implemented in Sprint 4.
        """

        leads: list[Lead] = []

        
        return ProcessorResult(
                leads=[],
                stats=ParserStatistics(),
            )