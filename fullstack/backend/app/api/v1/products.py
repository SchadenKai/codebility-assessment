from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.engine import get_session
from app.models.products import (
    CreateProductModel,
    ProductModel,
    PublicProductModel,
    UpdateProductModel,
)


router = APIRouter(prefix="/products", tags=["products"])
admin_router = APIRouter(prefix="/admin/products", tags=["products", "admin"])


@admin_router.post("")
def create_product_api(
    req: CreateProductModel, db_session: Session = Depends(get_session)
) -> ProductModel:
    pass


@admin_router.get("")
def list_products_for_admin_api(
    db_session: Session = Depends(get_session),
) -> list[PublicProductModel]:
    pass


@admin_router.patch("/{id}")
def update_product_api(req: UpdateProductModel, id: int) -> ProductModel:
    pass


@admin_router.delete("/{id}")
def delete_product_api(id: int) -> None:
    pass


@router.get("/{id}")
def get_product_api(id: int) -> PublicProductModel:
    pass


@router.get("")
def list_products_for_users_api() -> list[PublicProductModel]:
    pass
