import hashlib
from uuid import uuid4

from src.models.lead import Lead
from src.models.enums import DatasetType

from src.utils.phone import PhoneUtils
from src.utils.email import EmailUtils
from src.utils.text import TextUtils


class LeadBuilder:

    @staticmethod
    def _generate_key(
        email: str,
        phone: str,
        name: str,
        company: str,
    ) -> str:

        email = EmailUtils.normalize(email)

        if email:
            return hashlib.sha256(email.encode()).hexdigest()

        phone = PhoneUtils.normalize(phone)

        if phone:
            return hashlib.sha256(phone.encode()).hexdigest()

        text = (
            TextUtils.lower(name)
            + "|"
            + TextUtils.lower(company)
        )

        if text != "|":
            return hashlib.sha256(text.encode()).hexdigest()

        return str(uuid4())

    @classmethod
    def create(
        cls,
        dataset: DatasetType,
        name: str = "",
        email: str = "",
        phone: str = "",
        company: str = "",
        assigned_to: str = "",
        metadata: dict | None = None,
    ) -> Lead:

        return Lead(
            lead_id=str(uuid4()),
            lead_key=cls._generate_key(
                email=email,
                phone=phone,
                name=name,
                company=company,
            ),
            name=TextUtils.clean(name),
            email=EmailUtils.normalize(email),
            phone=PhoneUtils.normalize(phone),
            company=TextUtils.clean(company),
            assigned_to=TextUtils.clean(assigned_to),
            datasets={dataset},
            metadata=metadata or {},
        )