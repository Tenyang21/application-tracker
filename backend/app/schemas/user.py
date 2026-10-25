from pydantic import BaseModel
from typing import Optional

#schema defines the shape of data going in and out of the API
class UserCreate(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True

class UserOut(BaseModel):
    user_id: int
    email: str
    
    class Config:
        orm_mode = True
    
class UserResponse(BaseModel):
    user_id: int
    email: str

    class Config:
        orm_mode = True