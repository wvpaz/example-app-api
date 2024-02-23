from fastapi import APIRouter
from src.routers.user_router import UserRouter

routers = APIRouter()

routers.include_router(UserRouter)