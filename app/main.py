from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from sqlalchemy import text
from app.core.config import setting
from app.core.db import engine
from app.api.v1 import api

@asynccontextmanager
async def lifeSpan(app:FastAPI):
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("✅ Database connected successfully!")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        # You could also raise an error here to stop the server from starting
    
    yield

app = FastAPI(
    lifespan=lifeSpan
)


app.add_middleware(
    CORSMiddleware,
    # allow_origins=["hhtp://localhost:3000"],
)

app.include_router(api.api_routes,prefix="/api/v1")