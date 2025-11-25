from typing import cast
from fastapi import Depends
from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from app.models.products import (
    CreateProductModel,
    ProductModel,
    PublicProductModel,
    UpdateProductModel,
)
from app.repository.models import Product
from app.core.engine import get_session


class ProductsRepository:
    def __init__(self, db_session: Session = Depends(get_session)) -> None:
        self._db_session = db_session

    def create_product(self, new_product: CreateProductModel) -> ProductModel:
        product = Product(**new_product.model_dump())
        self._db_session.add(product)
        self._db_session.commit()
        self._db_session.refresh()
        return product

    def batch_create_products(
        self, new_products: list[CreateProductModel]
    ) -> bool | None:
        products = [Product(**new_product.model_dump()) for new_product in new_products]
        self._db_session.add_all(products)
        self._db_session.commit()
        return True

    def list_products_for_admin(
        self, items: int, page: int = 1
    ) -> list[ProductModel] | None:
        offset = (page - 1) * items
        stmt = select(Product).order_by(Product.id).limit(items).offset(offset)
        products = self._db_session.execute(stmt).all()
        return products

    def list_products_for_users(
        self, items: int, page: int = 1
    ) -> list[PublicProductModel] | None:
        offset = (page - 1) * items
        stmt = select(Product).order_by(Product.id).limit(items).offset(offset)
        products = self._db_session.execute(stmt).all()
        # check if pydantic will automatically shape this / is it better to filter the columns out
        return products

    def get_product_for_admin(self, product_id: int) -> ProductModel:
        stmt = select(Product).where(Product.id == product_id).distinct()
        product = self._db_session.query(stmt)
        return product

    def get_product_for_users(self, product_id: int) -> PublicProductModel | None:
        stmt = select(Product).where(Product.id == product_id).distinct()
        product = self._db_session.query(stmt)
        return product

    def update_product(
        self, product_id: int, updated_product: UpdateProductModel
    ) -> ProductModel | None:
        product = self._db_session.query(
            select(Product).where(Product.id == product_id)
        )
        if product is None or product.rowcount == 0:
            return None

        product = cast(Product, product)
        product.product_name = updated_product.product_name
        product.details = updated_product.details
        product.image_url = updated_product.image_url
        product.price = updated_product.price
        product.stock = updated_product.stock

        self._db_session.add(product)
        self._db_session.commit()
        self._db_session.refresh()
        return product

    def delete_product(self, product_id: int) -> bool | None:
        stmt = delete(Product).where(Product.id == product_id)
        product = self._db_session.execute(stmt)
        if product.rowcount == 0:
            return None
        return True
