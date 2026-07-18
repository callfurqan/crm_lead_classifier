from pathlib import Path

import pandas as pd

from config import OUTPUT_DIR
from src.models.enums import ClassificationStatus, DatasetType
from src.models.lead import Lead


class ExcelExporter:
    """
    Writes classified leads to Excel files.
    Contains no classification logic — formatting only.
    """

    DATASET_PREFIX = {
        DatasetType.SMS: "sms",
        DatasetType.EMAIL: "emails",
        DatasetType.CALL: "calls",
    }

    COLUMNS = [
        "lead_id",
        "name",
        "phone",
        "email",
        "company",
        "assigned_to",
        "status",
        "level",
        "confidence",
        "reason",
        "classifier",
        "conversation_text",
    ]

    def __init__(self, output_dir: Path | None = None):
        self.output_dir = output_dir or OUTPUT_DIR
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def export(self, leads: list[Lead]) -> list[Path]:

        written: list[Path] = []

        by_dataset: dict[DatasetType, list[Lead]] = {
            DatasetType.SMS: [],
            DatasetType.EMAIL: [],
            DatasetType.CALL: [],
        }

        for lead in leads:
            for dataset in lead.datasets:
                if dataset in by_dataset:
                    by_dataset[dataset].append(lead)

        for dataset, dataset_leads in by_dataset.items():

            if not dataset_leads:
                continue

            prefix = self.DATASET_PREFIX[dataset]

            interested = [
                lead
                for lead in dataset_leads
                if lead.classification.status
                == ClassificationStatus.INTERESTED
            ]

            non_interested = [
                lead
                for lead in dataset_leads
                if lead.classification.status
                != ClassificationStatus.INTERESTED
            ]

            written.append(
                self._write_file(
                    f"{prefix}_interested.xlsx",
                    interested,
                )
            )

            written.append(
                self._write_file(
                    f"{prefix}_non_interested.xlsx",
                    non_interested,
                )
            )

        return written

    def _write_file(self, filename: str, leads: list[Lead]) -> Path:

        path = self.output_dir / filename

        rows = [self._lead_to_row(lead) for lead in leads]

        df = pd.DataFrame(rows, columns=self.COLUMNS)
        df.to_excel(path, index=False)

        return path

    @staticmethod
    def _lead_to_row(lead: Lead) -> dict:

        classification = lead.classification

        return {
            "lead_id": lead.lead_id,
            "name": lead.name,
            "phone": lead.phone,
            "email": lead.email,
            "company": lead.company,
            "assigned_to": lead.assigned_to,
            "status": classification.status.value,
            "level": classification.level.value,
            "confidence": classification.confidence,
            "reason": classification.reason,
            "classifier": classification.classifier,
            "conversation_text": lead.conversation_text,
        }
