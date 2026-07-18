from dataclasses import dataclass

from src.core.parser_statistics import ParserStatistics
from src.models.lead import Lead


@dataclass
class ProcessorResult:
    leads: list[Lead]
    stats: ParserStatistics