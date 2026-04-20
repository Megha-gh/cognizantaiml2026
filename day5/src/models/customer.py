
from pydantic import BaseModel, Field, EmailStr
from src.models.full_name import FullName

class Customer(BaseModel):
    customer_id: int = Field(..., gt=0, description="Unique identifier for the customer")
    name: FullName
    email: EmailStr = Field(..., description="Email address of the customer")
    phone_no: int = Field(..., ge=1000000000, le=10000000000, description="Phone number of the customer")
