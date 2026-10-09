from fastapi import FastAPI
from src.routers import conversion_router

app = FastAPI()

app.include_router(conversion_router.router)
