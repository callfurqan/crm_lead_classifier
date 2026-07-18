from dataclasses import dataclass


@dataclass
class ParserStatistics:

    loaded: int = 0

    parsed: int = 0

    skipped: int = 0

    errors: int = 0

    interactions: int = 0

    @property
    def average_interactions(self):

        if self.parsed == 0:
            return 0

        return round(
            self.interactions / self.parsed,
            2
        )