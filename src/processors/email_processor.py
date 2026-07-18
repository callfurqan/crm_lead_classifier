from src.models.enums import DatasetType

from src.core.parser_statistics import ParserStatistics
from src.core.processor_result import ProcessorResult

from .base_processor import BaseProcessor


class EmailProcessor(BaseProcessor):
    """
    Converts Email conversations into normalized Lead objects.
    """

    DIRECTION_MAP = {
        "1": "outbound",
        "4": "inbound",
        "6": "inbound",
    }

    def process(self, data: dict) -> ProcessorResult:

        leads = []
        stats = ParserStatistics()

        conversations = data.get("conversations", [])

        for conversation in conversations:

            stats.loaded += 1

            try:

                lead = self.build_lead(
                    dataset=DatasetType.EMAIL,
                    name=(
                        conversation.get("contact_name")
                        or conversation.get("name", "")
                    ),
                    email=conversation.get("primary_email", ""),
                    phone="",
                    company=conversation.get("contact_company", ""),
                    assigned_to="",
                    metadata={
                        "conversation_index": conversation.get("index"),
                        "page": conversation.get("page"),
                        "sidebar_index": conversation.get("sidebar_index"),
                        "subject": conversation.get("subject"),
                        "sequence": conversation.get("sequence"),
                        "last_message_time": conversation.get("last_message_time"),
                        "email_count": conversation.get("email_count", 0),
                    },
                )

                emails = conversation.get("emails", [])

                # --------------------------------------------------
                # Case 1 : Full email thread available
                # --------------------------------------------------

                if emails:

                    for email in emails:

                        try:

                            direction = self.DIRECTION_MAP.get(
                                str(email.get("direction")),
                                "outbound",
                            )

                            interaction = self.build_interaction(
                                source="email",
                                direction=direction,
                                sender=email.get("from_name", ""),
                                receiver=email.get("to", ""),
                                timestamp=email.get("timestamp"),
                                subject=conversation.get("subject", ""),
                                content=email.get("body", ""),
                                metadata={
                                    "from_email": email.get("from_email"),
                                    "to_email": email.get("to"),
                                    "sender": email.get("sender"),
                                    "source": email.get("source"),
                                },
                            )

                            lead.interactions.append(interaction)

                        except Exception:
                            stats.errors += 1

                # --------------------------------------------------
                # Case 2 : No thread exported
                # Create one synthetic interaction from preview
                # --------------------------------------------------

                else:

                    preview = conversation.get(
                        "last_message_preview",
                        "",
                    )

                    if preview:

                        interaction = self.build_interaction(
                            source="email",
                            direction="inbound",
                            sender=conversation.get("name", ""),
                            receiver="",
                            timestamp=conversation.get(
                                "last_message_time"
                            ),
                            subject=conversation.get("subject", ""),
                            content=preview,
                            metadata={
                                "synthetic": True,
                                "source": "preview",
                            },
                        )

                        lead.interactions.append(interaction)

                stats.parsed += 1
                stats.interactions += len(lead.interactions)

                leads.append(lead)

            except Exception as exc:

                stats.errors += 1

                print(
                    f"[EmailProcessor] "
                    f"Skipping conversation "
                    f"{conversation.get('index')} : {exc}"
                )

        return ProcessorResult(
            leads=leads,
            stats=stats,
        )