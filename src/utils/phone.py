import re


class PhoneUtils:

    @staticmethod
    def normalize(phone: str | None) -> str:
        if not phone:
            return ""

        digits = re.sub(r"\D", "", phone)

        return digits

    @staticmethod
    def is_valid(phone: str | None) -> bool:
        digits = PhoneUtils.normalize(phone)

        return len(digits) >= 10