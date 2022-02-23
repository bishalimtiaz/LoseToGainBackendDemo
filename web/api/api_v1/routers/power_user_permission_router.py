from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from security.database import get_db
from web.api.api_v1.repositories import power_user_permission_repo
from schemas import power_user_permission_schema

router = APIRouter(
    prefix='/power_user/permission',
    tags=["Web/power_user_permission"]
)


# assign permission to a power user
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_power_user_permission(
        power_user_permission: power_user_permission_schema.CreatePowerUserPermission,
        db: Session = Depends(get_db)
):
    return power_user_permission_repo.create_power_user_permission(power_user_permission, db)


# check permissions given a user
@router.get('/', status_code=status.HTTP_200_OK, response_model=power_user_permission_schema.ShowPowerUserPermission)
def fetch_Permissions(
        id,
        db: Session = Depends(get_db)
):
    return power_user_permission_repo.fetch_Permissions(id, db)
