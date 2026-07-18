from src.models.lead import Lead
from src.models.enums import DatasetType
from .base_processor import BaseProcessor
from src.core.parser_statistics import ParserStatistics
from src.core.processor_result import ProcessorResult


class SMSProcessor(BaseProcessor):
    """
    Converts SMS conversations JSON into normalized Lead objects.
    """

    def process(self, data: dict) -> list[Lead]:

        leads: list[Lead] = []

        stats = ParserStatistics()

        conversations = data.get("conversations", [])

        for conversation in conversations:

            stats.loaded += 1

            try:
                lead = self.build_lead(
                    dataset=DatasetType.SMS,
                    name=conversation.get("name", ""),
                    phone=conversation.get("phone", ""),
                    email=conversation.get("email", ""),
                    assigned_to=conversation.get("assigned_to", ""),
                    metadata={
                        "conversation_id": conversation.get("id"),
                        "message_count": conversation.get("message_count"),
                        "last_message_preview": conversation.get(
                            "last_message_preview"
                        ),
                    },
                )

                messages = conversation.get("messages", [])

                for message in messages:

                    interaction = self.build_interaction(
                        source="sms",
                        direction=message.get("direction", "outbound"),
                        sender=message.get("sender", ""),
                        receiver=conversation.get("assigned_to", ""),
                        timestamp=message.get("timestamp"),
                        content=message.get("text", ""),
                        metadata={
                            "message_id": message.get("id"),
                            "sender_phone": message.get("sender_phone"),
                            "source": message.get("source"),
                            "status": message.get("status"),
                        },
                    )

                    if not messages:
                        stats.skipped += 1
                        continue

                    lead.interactions.append(interaction)

                leads.append(lead)

                stats.parsed += 1

                stats.interactions += len(messages)

            except Exception as exc:

                stats.errors += 1

                print(...)
                print(
                    f"[SMSProcessor] Skipping conversation "
                    f"{conversation.get('id')} : {exc}"
                )


        return ProcessorResult(
            leads=leads,
            stats=stats,
        )    
