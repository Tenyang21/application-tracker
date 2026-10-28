from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing import Optional

#schema defines the shape of data going in and out of the API
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    created_at = datetime

#what login returns
class Token(BaseModel):
    access_token: str
    token_type = str = "bearer"