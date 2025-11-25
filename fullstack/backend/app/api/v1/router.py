from fastapi import APIRouter
from .products import router as products_router
from .products import admin_router as admin_products_router

router = APIRouter(prefix="/v1", tags=["v1"])

router.include_router(products_router)
router.include_router(admin_products_router)
