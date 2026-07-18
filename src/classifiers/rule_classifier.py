from src.classifiers.base_classifier import BaseClassifier
from src.classifiers.keyword_rules import (
    CALLBACK_KEYWORDS,
    INTERESTED_KEYWORDS,
    NEGATIVE_KEYWORDS,
)
from src.models.enums import ClassificationStatus, InterestLevel
from src.models.lead import Lead


class RuleClassifier(BaseClassifier):
    """
    Rule-based keyword classifier.

    Priority (highest score wins):
      Wrong Number > Not Interested > Interested > Callback > Unknown

    Interested outranks Callback when both match, e.g.
    "I'm interested, call me tomorrow." → Interested
    """

    WRONG_NUMBER_KEYWORDS = ["wrong number"]

    # Priority scores — higher wins when multiple categories match
    SCORE_WRONG_NUMBER = 100
    SCORE_NOT_INTERESTED = 90
    SCORE_INTERESTED = 80
    SCORE_CALLBACK = 70

    def classify(self, lead: Lead):

        text = (lead.conversation_text or "").lower()

        matches = []

        for keyword in self.WRONG_NUMBER_KEYWORDS:
            if keyword in text:
                matches.append(
                    (
                        self.SCORE_WRONG_NUMBER,
                        ClassificationStatus.WRONG_NUMBER,
                        InterestLevel.UNKNOWN,
                        keyword,
                    )
                )

        for keyword in NEGATIVE_KEYWORDS:
            if keyword in self.WRONG_NUMBER_KEYWORDS:
                continue
            if keyword in text:
                matches.append(
                    (
                        self.SCORE_NOT_INTERESTED,
                        ClassificationStatus.NON_INTERESTED,
                        InterestLevel.LOW,
                        keyword,
                    )
                )

        for keyword in INTERESTED_KEYWORDS:
            if keyword in text:
                matches.append(
                    (
                        self.SCORE_INTERESTED,
                        ClassificationStatus.INTERESTED,
                        InterestLevel.MEDIUM,
                        keyword,
                    )
                )

        for keyword in CALLBACK_KEYWORDS:
            if keyword in text:
                matches.append(
                    (
                        self.SCORE_CALLBACK,
                        ClassificationStatus.CALLBACK,
                        InterestLevel.LOW,
                        keyword,
                    )
                )

        if not matches:
            lead.classification.status = ClassificationStatus.UNKNOWN
            lead.classification.level = InterestLevel.UNKNOWN
            lead.classification.reason = "No keyword matched"
            lead.classification.confidence = 0.0
            lead.classification.classifier = "rule"
            return lead

        # Highest priority score wins; longer keyword preferred on ties
        matches.sort(key=lambda m: (m[0], len(m[3])), reverse=True)
        _, status, level, keyword = matches[0]

        lead.classification.status = status
        lead.classification.level = level
        lead.classification.reason = f'Matched keyword: "{keyword}"'
        lead.classification.confidence = self._confidence(keyword)
        lead.classification.classifier = "rule"

        return lead

    @staticmethod
    def _confidence(keyword: str) -> float:
        return min(0.99, round(0.70 + len(keyword) * 0.02, 2))
