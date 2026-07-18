# from src.utils.phone import PhoneUtils
# from src.utils.email import EmailUtils
# from src.utils.text import TextUtils
# from src.utils.datetime_utils import DateTimeUtils

# print(PhoneUtils.normalize("(646) 123-4567"))
# print(EmailUtils.normalize(" TEST@GMAIL.COM "))
# print(TextUtils.clean("<b>Hello</b>\n\nWorld"))
# print(DateTimeUtils.format("2026-01-12 10:30"))


from src.builders.lead_builder import LeadBuilder
from src.models.enums import DatasetType

lead = LeadBuilder.create(
    dataset=DatasetType.SMS,
    name=" John Doe ",
    phone="(646) 123-4567",
    email="John@GMAIL.com",
    company=" ABC LLC "
)

print(lead)