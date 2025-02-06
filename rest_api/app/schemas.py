from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserBase(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=50)
    last_name: Optional[str] = Field(..., min_length=2, max_length=50)
    email: EmailStr
    gender: Optional[str] = Field(None, pattern="^(Male|Female|Non-binary|Genderqueer|Bigender|Polygender|Genderfluid|Other)?$")
    ip_address: Optional[str] = Field(None, pattern=r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    country_code: Optional[str] = Field(None, max_length=3, pattern=r"^[A-Z]{2,3}$")

    class Config:
        json_schema_extra = {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com",
                "gender": "Male",
                "ip_address": "192.168.1.1",
                "country_code": "US"
            }
        }


class UserCreate(UserBase):
    id: int
    pass

class UserUpdate(UserBase):
    id: int
    # optional fields
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    gender: Optional[str]
    ip_address: Optional[str]
    country_code: Optional[str]

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True
