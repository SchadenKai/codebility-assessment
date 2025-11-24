from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from app.repository.models import Product, User
from typing import List, Optional

class ProductRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create(self, product_data: dict, user: User) -> Product:
        new_product = Product(**product_data, updated_by=user.id)
        self.db_session.add(new_product)
        await self.db_session.commit()
        await self.db_session.refresh(new_product)
        return new_product

    async def get_by_id(self, product_id: int) -> Optional[Product]:
        result = await self.db_session.execute(select(Product).where(Product.id == product_id))
        return result.scalars().first()

    async def list(
        self, page: int = 1, limit: int = 10, search: Optional[str] = None
    ) -> List[Product]:
        query = select(Product)
        if search:
            query = query.where(Product.product_name.ilike(f"%{search}%"))
        
        offset = (page - 1) * limit
        query = query.offset(offset).limit(limit)
        
        result = await self.db_session.execute(query)
        return result.scalars().all()

    async def update(self, product_id: int, update_data: dict, user: User) -> Optional[Product]:
        update_data['updated_by'] = user.id
        
        stmt = (
            update(Product)
            .where(Product.id == product_id)
            .values(**update_data)
            .returning(Product)
        )
        result = await self.db_session.execute(stmt)
        await self.db_session.commit()
        return result.scalars().first()

    async def delete(self, product_id: int) -> bool:
        stmt = delete(Product).where(Product.id == product_id)
        result = await self.db_session.execute(stmt)
        await self.db_session.commit()
        return result.rowcount > 0
