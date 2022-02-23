from fastapi import APIRouter

from web.api.api_v1.routers import user_role_router, power_user_router, power_user_permission_router, \
    authentication_router

api_router = APIRouter(
    prefix='/api/web/v1'
)

api_router.include_router(user_role_router.router)
api_router.include_router(power_user_router.router)
api_router.include_router(power_user_permission_router.router)
api_router.include_router(authentication_router.router)
