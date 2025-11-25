from fastapi import Depends
from sqlalchemy.orm import Session

from app.repository.products import ProductsRepository


class ProductsService:
    def __init__(self, repo: ProductsRepository = Depends()) -> None:
        self.repo = repo

    def create_product():
        pass

    def batch_create_products():
        pass

    def list_producuts():
        pass

    def get_product():
        pass

    def update_product():
        pass

    def delete_product(self, product_id: int) -> bool:
        return self.repo.delete_product(product_id)
