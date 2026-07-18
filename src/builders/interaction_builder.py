from src.models.enums import (
    InteractionDirection,
    InteractionSource,
)
from src.models.interaction import Interaction
from src.utils.datetime_utils import DateTimeUtils
from src.utils.text import TextUtils


class InteractionBuilder:

    @staticmethod
    def create(
        source,
        direction,
        sender="",
        receiver="",
        timestamp=None,
        content="",
        metadata=None,
    ) -> Interaction:

        if isinstance(source, str):
            source = InteractionSource(source.lower())

        if isinstance(direction, str):
            direction = InteractionDirection(direction.lower())

        return Interaction(
            source=source,
            direction=direction,
            timestamp=DateTimeUtils.parse(timestamp),
            sender=TextUtils.clean(sender),
            receiver=TextUtils.clean(receiver),
            content=TextUtils.clean(content),
            metadata=metadata or {},
        )