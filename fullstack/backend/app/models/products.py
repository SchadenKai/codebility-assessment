from datetime import datetime
import uuid
from pydantic import BaseModel


class ProductModel(BaseModel):
    id: int
    product_name: str
    details: str | None = None
    image_url: str | None = None
    created_at: datetime
    updated_at: datetime
    updated_by: uuid.UUID
    created_by: uuid.UUID
    price: float
    stock: int


class PublicProductModel(BaseModel):
    id: int
    product_name: str
    details: str | None = None
    image_url: str | None = None
    price: float
    stock: int
    created_at: datetime
    updated_at: datetime


class CreateProductModel(BaseModel):
    product_name: str
    details: str | None = None
    image_url: str | None = None
    price: float
    stock: int


class UpdateProductModel(BaseModel):
    product_name: str | None = None
    details: str | None = None
    image_url: str | None = None
    price: float | None = None
    stock: int | None = None
