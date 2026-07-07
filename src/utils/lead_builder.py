from uuid import uuid4

from src.models.lead import Lead
from src.models.enums import DatasetType


class LeadBuilder:

    @staticmethod
    def create(dataset: DatasetType) -> Lead:

        return Lead(
            lead_id=str(uuid4()),
            lead_key="",
            datasets={dataset},
        )