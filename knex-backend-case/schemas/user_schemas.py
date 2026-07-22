from pydantic import BaseModel, EmailStr, Field
from typing import Literal

class UserCreate(BaseModel):
    name: str = Field(min_length=1)
    email: EmailStr
    password: str = Field(min_length=1)
    role: Literal["client", "seller"]

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1)
    