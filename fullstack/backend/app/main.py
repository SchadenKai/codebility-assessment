from collections.abc import AsyncGenerator
from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.engine import warm_up_connections
from app.api.v1 import users, products, carts


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    print("API lifespan started")
    await warm_up_connections()
    # TODO: warmup database and cache connections
    yield
    # close all connections
    print("API lifespan ended")


app = FastAPI(title="e-commerce app api server", version="0.1.0", lifespan=lifespan)

app.include_router(users.router, prefix="/api/v1", tags=["users"])
app.include_router(products.router, prefix="/api/v1/products", tags=["products"])
app.include_router(carts.router, prefix="/api/v1/cart", tags=["cart"])


@app.get("/health")
async def health_check():
    return {"status": "ok"}
