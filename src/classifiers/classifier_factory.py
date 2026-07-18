from src.classifiers.base_classifier import BaseClassifier
from src.classifiers.rule_classifier import RuleClassifier


class ClassifierFactory:

    @staticmethod
    def create() -> BaseClassifier:
        return RuleClassifier()
