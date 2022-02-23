from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from security.database import get_db
from schemas import power_user_schema
from web.api.api_v1.repositories import authentication_repo

router = APIRouter(
    prefix='/auth',
    tags=["Web/auth"]
)


@router.post('/')
def login(request_user: power_user_schema.AuthenticatePowerUser, db: Session = Depends(get_db)):
    return authentication_repo.authenticate(request_user, db)
