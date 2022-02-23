from fastapi import APIRouter, Security
from fastapi import Depends
from sqlalchemy.orm import Session

from constants.role import Role
from security.database import get_db
from security.oauth2 import get_current_user
from web.api.api_v1.repositories import user_role_repo
from schemas import user_role_schema, power_user_schema

router = APIRouter(
    prefix='/role',
    tags=["Web/user_role"]
)


@router.post('/')
def create_user_role(request_user_role: user_role_schema.UserRole, db: Session = Depends(get_db)):
    return user_role_repo.create_user_role(request_user_role, db)


@router.get('/')
def get_user_role(
        db: Session = Depends(get_db),
        current_user: power_user_schema.ShowPowerUser = Security(
            get_current_user,
            scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
        ),

):
    return user_role_repo.get_user_role(db)
