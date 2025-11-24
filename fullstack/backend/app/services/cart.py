from sqlalchemy.ext.asyncio import AsyncSession
from app.repository.models import Cart, User
from app.schemas import CartItemCreate, CartItemUpdate
from app.repository.carts import CartRepository
from app.repository.products import ProductRepository
from typing import List, Optional

class CartService:
    def __init__(self, db_session: AsyncSession):
        self.cart_repo = CartRepository(db_session)
        self.product_repo = ProductRepository(db_session)

    async def add_to_cart(self, item_data: CartItemCreate, user: User) -> Cart:
        product = await self.product_repo.get_by_id(item_data.product_id)
        if not product:
            raise ValueError("Product not found")

        cart_item = await self.cart_repo.get_by_user_and_product(user.id, item_data.product_id)

        if cart_item:
            return await self.cart_repo.update_quantity(cart_item, item_data.quantity)
        else:
            return await self.cart_repo.create(user.id, item_data.product_id, item_data.quantity)

    async def get_cart_items(self, user: User) -> List[Cart]:
        return await self.cart_repo.list_by_user(user.id)

    async def update_cart_item(self, item_id: int, item_data: CartItemUpdate, user: User) -> Optional[Cart]:
        return await self.cart_repo.update(item_id, user.id, item_data.quantity)

    async def remove_from_cart(self, item_id: int, user: User) -> bool:
        return await self.cart_repo.delete(item_id, user.id)
