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