import re
from bs4 import BeautifulSoup


class TextUtils:
    """Utility methods for cleaning and normalizing text."""

    @staticmethod
    def strip_html(text: str | None) -> str:

        if not text:
            return ""

        # Parse only if HTML tags are present
        if "<" in text and ">" in text:
            return BeautifulSoup(
                text,
                "html.parser"
            ).get_text(
                separator=" ",
                strip=True,
            )

        return text

    @staticmethod
    def clean(text: str | None) -> str:
        if not text:
            return ""

        text = TextUtils.strip_html(text)

        text = text.replace("\r", " ")
        text = text.replace("\n", " ")

        text = re.sub(r"\s+", " ", text)

        return text.strip()

    @staticmethod
    def lower(text: str | None) -> str:
        return TextUtils.clean(text).lower()

    @staticmethod
    def is_empty(text: str | None) -> bool:
        return len(TextUtils.clean(text)) == 0

    @staticmethod
    def truncate(text: str, limit: int = 200) -> str:
        text = TextUtils.clean(text)

        if len(text) <= limit:
            return text

        return text[:limit] + "..."