import uvicorn
from fastapi import FastAPI
from src.routers import conversion_router, default_router

app = FastAPI()

app.include_router(conversion_router.router)
app.include_router(default_router.router)