from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session

from app.models.products import CreateProductModel, ProductModel, PublicProductModel, UpdateProductModel
from app.repository.models import Product
from app.exceptions import InternalServerException


class ProductsRepository:
    def __init__(self, db_session: Session) -> None:
        self._db_session = db_session

    def create_product(self, new_product: CreateProductModel):
        try:
            product = Product(**new_product.model_dump())
            self._db_session.add(product)
            self._db_session.commit()
            self._db_session.refresh()
            return product
        except Exception as e:
            raise InternalServerException(status_code=500, exception_message=e)

    def batch_create_products(self, new_products: list[CreateProductModel]) -> bool:
        try:
            products = [
                Product(**new_product.model_dump()) for new_product in new_products
            ]
            self._db_session.add_all(products)
            self._db_session.commit()
            return True
        except Exception as e:
            raise InternalServerException(status_code=500, exception_message=e)

    def list_products_for_admin(self, items: int, page: int = 1) -> list[ProductModel]:
        try:
            offset = (page - 1) * items
            stmt = select(Product).order_by(Product.id).limit(items).offset(offset)
            products = self._db_session.execute(stmt).all()
            return products
        except Exception as e:
            raise InternalServerException(status_code=500, exception_message=e)

    def list_products_for_users(
        self, items: int, page: int = 1
    ) -> list[PublicProductModel]:
        try:
            offset = (page - 1) * items
            stmt = select(Product).order_by(Product.id).limit(items).offset(offset)
            products = self._db_session.execute(stmt).all()
            # check if pydantic will automatically shape this / is it better to filter the columns out
            return products
        except Exception as e:
            raise InternalServerException(status_code=500, exception_message=e)

    def get_product_for_admin(self, product_id: int) -> ProductModel:
        try:
            stmt = select(Product).where(Product.id == product_id).distinct()
            product = self._db_session.query(stmt)
            return product
        except Exception as e:
            raise InternalServerException(status_code=500, exception_message=e)

    def get_product_for_users(self, product_id: int) -> PublicProductModel:
        try:
            stmt = select(Product).where(Product.id == product_id).distinct()
            product = self._db_session.query(stmt)
            return product
        except Exception as e:
            raise InternalServerException(status_code=500, exception_message=e)

    def update_product(self, product_id: int, updated_product: UpdateProductModel):
        try:
            stmt = update(Product).where(Product.id == product_id).values()
            product = self._db_session.query(stmt)
            return product
        except Exception as e:
            raise InternalServerException(status_code=500, exception_message=e)

    def delete_product(self, product_id: int):
        try:
            stmt = delete(Product).where(Product.id == product_id)
            product = self._db_session.query(stmt)
            return product
        except Exception as e:
            raise InternalServerException(status_code=500, exception_message=e)
