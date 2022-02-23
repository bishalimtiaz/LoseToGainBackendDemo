from fastapi import APIRouter
from mobile.api.api_v1.routers import authentication_router, end_user_router

api_router = APIRouter(
    prefix='/api/mobile/v1'
)

api_router.include_router(authentication_router.router)
api_router.include_router(end_user_router.router)
