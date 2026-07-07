from src.models.enums import DatasetType


class DatasetDetector:

    @staticmethod
    def detect(data):

        if isinstance(data, dict):

            if "conversations" in data:

                conversations = data["conversations"]

                if conversations:

                    sample = conversations[0]

                    if "emails" in sample:
                        return DatasetType.EMAIL

                    if "messages" in sample:
                        return DatasetType.SMS

            if "calls" in data:
                return DatasetType.CALL

        return None