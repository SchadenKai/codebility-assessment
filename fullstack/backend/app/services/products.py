from sqlalchemy.ext.asyncio import AsyncSession
from app.repository.models import Product, User
from app.schemas import ProductCreate, ProductUpdate
from app.repository.products import ProductRepository
from typing import List, Optional

class ProductService:
    def __init__(self, db_session: AsyncSession):
        self.repo = ProductRepository(db_session)

    async def create_product(self, product_data: ProductCreate, user: User) -> Product:
        return await self.repo.create(product_data.dict(), user)

    async def get_product(self, product_id: int) -> Optional[Product]:
        return await self.repo.get_by_id(product_id)

    async def list_products(
        self, page: int = 1, limit: int = 10, search: Optional[str] = None
    ) -> List[Product]:
        return await self.repo.list(page=page, limit=limit, search=search)

    async def update_product(self, product_id: int, product_data: ProductUpdate, user: User) -> Optional[Product]:
        update_data = product_data.dict(exclude_unset=True)
        return await self.repo.update(product_id, update_data, user)

    async def delete_product(self, product_id: int) -> bool:
        return await self.repo.delete(product_id)
