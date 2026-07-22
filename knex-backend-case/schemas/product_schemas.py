from pydantic import BaseModel, Field
from decimal import Decimal

class ProductCreate(BaseModel):
    name: str = Field(min_length=1)
    description: str = Field(min_length=1)
    price: Decimal = Field(gt=0)
    stock: int = Field(ge=0)

class ProductUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: Decimal | None = Field(default=None, gt=0)
    stock: int | None = Field(default=None, ge=0)