from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from app.repository.models import Cart
from typing import List, Optional


class CartRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_by_user_and_product(
        self, user_id: int, product_id: int
    ) -> Optional[Cart]:
        result = await self.db_session.execute(
            select(Cart).where(Cart.user_id == user_id, Cart.product_id == product_id)
        )
        return result.scalars().first()

    async def create(self, user_id: int, product_id: int, quantity: int) -> Cart:
        cart_item = Cart(
            user_id=user_id,
            product_id=product_id,
            quantity=quantity,
        )
        self.db_session.add(cart_item)
        await self.db_session.commit()
        await self.db_session.refresh(cart_item)
        return cart_item

    async def update_quantity(self, cart_item: Cart, quantity: int) -> Cart:
        cart_item.quantity += quantity
        await self.db_session.commit()
        await self.db_session.refresh(cart_item)
        return cart_item

    async def list_by_user(self, user_id: int) -> List[Cart]:
        result = await self.db_session.execute(
            select(Cart).where(Cart.user_id == user_id)
        )
        return result.scalars().all()

    async def update(self, item_id: int, user_id: int, quantity: int) -> Optional[Cart]:
        stmt = (
            update(Cart)
            .where(Cart.id == item_id, Cart.user_id == user_id)
            .values(quantity=quantity)
            .returning(Cart)
        )
        result = await self.db_session.execute(stmt)
        await self.db_session.commit()
        return result.scalars().first()

    async def delete(self, item_id: int, user_id: int) -> bool:
        stmt = delete(Cart).where(Cart.id == item_id, Cart.user_id == user_id)
        result = await self.db_session.execute(stmt)
        await self.db_session.commit()
        return result.rowcount > 0
