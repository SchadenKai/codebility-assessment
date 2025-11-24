from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.core.engine import get_async_session
from app.core.users import current_active_user
from app.repository.models import User
from app.schemas import CartItemCreate, CartItemRead, CartItemUpdate
from app.services.cart import CartService

router = APIRouter()

@router.post("/", response_model=CartItemRead, status_code=201)
async def add_to_cart(
    item: CartItemCreate,
    user: User = Depends(current_active_user),
    db: AsyncSession = Depends(get_async_session),
):
    cart_service = CartService(db)
    try:
        cart_item = await cart_service.add_to_cart(item_data=item, user=user)
        return cart_item
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/", response_model=List[CartItemRead])
async def get_cart(
    user: User = Depends(current_active_user),
    db: AsyncSession = Depends(get_async_session),
):
    cart_service = CartService(db)
    return await cart_service.get_cart_items(user=user)


@router.put("/{item_id}", response_model=CartItemRead)
async def update_cart_item(
    item_id: int,
    item: CartItemUpdate,
    user: User = Depends(current_active_user),
    db: AsyncSession = Depends(get_async_session),
):
    cart_service = CartService(db)
    updated_item = await cart_service.update_cart_item(
        item_id=item_id, item_data=item, user=user
    )
    if not updated_item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    return updated_item


@router.delete("/{item_id}", status_code=204)
async def delete_cart_item(
    item_id: int,
    user: User = Depends(current_active_user),
    db: AsyncSession = Depends(get_async_session),
):
    cart_service = CartService(db)
    success = await cart_service.remove_from_cart(item_id=item_id, user=user)
    if not success:
        raise HTTPException(status_code=404, detail="Cart item not found")
    return
