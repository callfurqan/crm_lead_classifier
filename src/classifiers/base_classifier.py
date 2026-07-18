from abc import ABC, abstractmethod

from src.models.lead import Lead


class BaseClassifier(ABC):

    @abstractmethod
    def classify(self, lead: Lead):
        pass
