import uuid
from fastapi_users import schemas
from pydantic import BaseModel, Field
from typing import Optional

class UserRead(schemas.BaseUser[uuid.UUID]):
    pass

class UserCreate(schemas.BaseUserCreate):
    pass

class UserUpdate(schemas.BaseUserUpdate):
    pass

class ProductRead(BaseModel):
    id: int
    product_name: str
    details: Optional[str] = None
    image_url: Optional[str] = None

    class Config:
        orm_mode = True

class ProductCreate(BaseModel):
    product_name: str
    details: Optional[str] = None
    image_url: Optional[str] = None

class ProductUpdate(BaseModel):
    product_name: Optional[str] = None
    details: Optional[str] = None
    image_url: Optional[str] = None

class CartItemRead(BaseModel):
    id: int
    product_id: int
    quantity: int
    product: ProductRead

    class Config:
        orm_mode = True

class CartItemCreate(BaseModel):
    product_id: int
    quantity: int = 1

class CartItemUpdate(BaseModel):
    quantity: int
