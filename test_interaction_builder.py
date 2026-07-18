from src.builders.interaction_builder import InteractionBuilder

interaction = InteractionBuilder.create(
    source="sms",
    direction="inbound",
    sender="John",
    receiver="Agent",
    timestamp="2026-07-08 10:30",
    content=" Hello, I need funding. "
)

print(interaction)