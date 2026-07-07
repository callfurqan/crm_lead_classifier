from abc import ABC, abstractmethod

from src.models.lead import Lead


class BaseProcessor(ABC):
    """
    Base class for all dataset processors.
    Every processor converts a JSON dataset into a list of Lead objects.
    """

    @abstractmethod
    def process(self, data: dict) -> list[Lead]:
        pass