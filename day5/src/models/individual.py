#create class individual using pydantic
from datetime import date
from pydantic import Field
from pydantic import FieldValidator
from src.models.customer import Customer
from src.models.gender import Gender

class Individual(Customer):
    gender: Gender
    dob:date = Field(..., description="Date of birth of the customer format YYYY-MM-DD")

@FieldValidator('dob')
def validate_dob(cls, value):
    if value >= date.today():
        raise ValueError("Date of birth must be in the past")
    return value
    age = (date.today() - value).days // 365
    if age < 18:
        raise ValueError("Customer must be at least 18 years old")
    return value