from collections.abc import AsyncGenerator
from fastapi import FastAPI
from contextlib import asynccontextmanager
from starlette.middleware.cors import CORSMiddleware

from app.api.v1.router import router as api_router_v1
from app.core.engine import warm_up_connections
from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    print("API lifespan started")
    await warm_up_connections()
    # TODO: warmup database and cache connections
    yield
    # close all connections
    print("API lifespan ended")


app = FastAPI(
    lifespan=lifespan, title="Codebility E-commerce API Server", version="v0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=settings.cors_allowed_origins,
    allow_credentials=True,
)

app.include_router(api_router_v1)


@app.get("/health")
async def health_check():
    return {"status": "ok"}
