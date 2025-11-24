from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional

from app.core.engine import get_async_session
from app.core.users import current_active_user, current_active_superuser
from app.repository.models import User
from app.schemas import ProductCreate, ProductRead, ProductUpdate
from app.services.products import ProductService

router = APIRouter()

@router.post("/", response_model=ProductRead, status_code=201)
async def create_product(
    product: ProductCreate,
    user: User = Depends(current_active_superuser),
    db: AsyncSession = Depends(get_async_session),
):
    product_service = ProductService(db)
    return await product_service.create_product(product_data=product, user=user)

@router.get("/", response_model=List[ProductRead])
async def list_products(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    search: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_async_session),
):
    product_service = ProductService(db)
    return await product_service.list_products(page=page, limit=limit, search=search)

@router.get("/{product_id}", response_model=ProductRead)
async def get_product(
    product_id: int,
    db: AsyncSession = Depends(get_async_session),
):
    product_service = ProductService(db)
    product = await product_service.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=ProductRead)
async def update_product(
    product_id: int,
    product: ProductUpdate,
    user: User = Depends(current_active_superuser),
    db: AsyncSession = Depends(get_async_session),
):
    product_service = ProductService(db)
    updated_product = await product_service.update_product(
        product_id=product_id, product_data=product, user=user
    )
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@router.delete("/{product_id}", status_code=204)
async def delete_product(
    product_id: int,
    user: User = Depends(current_active_superuser),
    db: AsyncSession = Depends(get_async_session),
):
    product_service = ProductService(db)
    product = await product_service.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    await product_service.delete_product(product_id)
    return
