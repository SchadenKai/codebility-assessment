from collections.abc import AsyncGenerator
from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.engine import warm_up_connections


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    print("API lifespan started")
    await warm_up_connections()
    # TODO: warmup database and cache connections
    yield
    # close all connections
    print("API lifespan ended")


app = FastAPI(lifespan=lifespan)


@app.get("/health")
async def health_check():
    return {"status": "ok"}
