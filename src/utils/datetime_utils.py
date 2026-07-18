from datetime import datetime
from dateutil import parser


class DateTimeUtils:

    @staticmethod
    def parse(value):
        if value is None:
            return None

        if isinstance(value, datetime):
            return value

        try:
            return parser.parse(str(value))
        except Exception:
            return None

    @staticmethod
    def format(value):

        dt = DateTimeUtils.parse(value)

        if dt is None:
            return ""

        return dt.strftime("%Y-%m-%d %H:%M:%S")