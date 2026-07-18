import re


class EmailUtils:

    EMAIL_REGEX = re.compile(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    )

    @staticmethod
    def normalize(email: str | None) -> str:
        if not email:
            return ""

        return email.strip().lower()

    @staticmethod
    def is_valid(email: str | None) -> bool:
        if not email:
            return False

        return EmailUtils.EMAIL_REGEX.fullmatch(
            EmailUtils.normalize(email)
        ) is not None