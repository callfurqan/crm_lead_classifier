from src.models.enums import DatasetType

from src.core.parser_statistics import ParserStatistics
from src.core.processor_result import ProcessorResult

from .base_processor import BaseProcessor


class CallProcessor(BaseProcessor):
    """
    Converts Call records into normalized Lead objects.
    """

    def process(self, data: dict) -> ProcessorResult:

        leads = []
        stats = ParserStatistics()

        records = data.get("calls", [])

        for record in records:

            stats.loaded += 1

            try:

                transcript = record.get("transcript", "") or ""
                notes = record.get("notes", "") or ""
                intent = record.get("intent", "") or ""
                disposition = record.get("disposition", "") or ""

                # ------------------------------------------------------
                # Build Lead
                # ------------------------------------------------------

                lead = self.build_lead(
                    dataset=DatasetType.CALL,
                    name=record.get("contact_name", ""),
                    phone=record.get("contact_phone", ""),
                    email="",
                    company=record.get("contact_company", ""),
                    assigned_to=record.get("user_name", ""),
                    metadata={
                        "record_id": record.get("id"),
                        "call_time": record.get("call_time"),
                        "duration": record.get("duration"),
                        "sentiment": record.get("sentiment"),
                        "intent": intent,
                        "disposition": disposition,
                        "has_transcript": record.get("has_transcript"),
                        "has_recording": record.get("has_recording"),
                    },
                )

                # ------------------------------------------------------
                # Determine interaction content
                # ------------------------------------------------------

                if transcript.strip():

                    content = transcript

                elif notes.strip():

                    content = notes

                else:

                    content = (
                        f"Intent: {intent}\n"
                        f"Disposition: {disposition}"
                    )

                # ------------------------------------------------------
                # Build Interaction
                # ------------------------------------------------------

                interaction = self.build_interaction(
                    source="call",
                    direction="inbound",
                    sender=record.get("contact_name", ""),
                    receiver=record.get("user_name", ""),
                    timestamp=record.get("call_time"),
                    subject="",
                    content=content,
                    metadata={
                        "duration": record.get("duration"),
                        "sentiment": record.get("sentiment"),
                        "intent": intent,
                        "disposition": disposition,
                        "mode": record.get("mode"),
                        "has_transcript": record.get("has_transcript"),
                        "has_recording": record.get("has_recording"),
                        "recording_url": record.get("recording_url"),
                        "user_phone": record.get("user_phone"),
                    },
                )

                lead.interactions.append(interaction)

                stats.parsed += 1
                stats.interactions += 1

                leads.append(lead)

            except Exception as exc:

                stats.errors += 1

                print(
                    f"[CallProcessor] "
                    f"Skipping record "
                    f"{record.get('id')} : {exc}"
                )

        return ProcessorResult(
            leads=leads,
            stats=stats,
        )