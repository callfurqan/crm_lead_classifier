from dataclasses import dataclass, field


@dataclass
class ExtractedInfo:

    funding_amount: str | None = None

    business_name: str | None = None

    business_type: str | None = None

    mca_balance: str | None = None

    callback_requested: bool = False

    callback_datetime: str | None = None

    documents_sent: bool = False

    decision_maker: bool | None = None

    questions: list[str] = field(default_factory=list)