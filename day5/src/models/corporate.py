#create corporate class inherit from customer
from pydantic import Field
from src.models.customer import Customer
from src.models.company_type import CompanyType

class Corporate(Customer):
    company_type: CompanyType
    registration_number: str = Field(..., pattern=r"^[A-Z0-9]+$", min_length=1, description="Registration number of the company")