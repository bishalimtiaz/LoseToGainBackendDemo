from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas import power_user_schema
from security.database import get_db
from web.api.api_v1.repositories import power_user_repo

router = APIRouter(
    prefix='/power_user',
    tags=["Web/power_user"]
)


# create power user
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_power_user(request_power_user: power_user_schema.CreatePowerUser, db: Session = Depends(get_db)):
    return power_user_repo.create_power_user(request_power_user, db)


# fetch power user
@router.get('/', status_code=status.HTTP_200_OK)
def fetch_power_user(id, db: Session = Depends(get_db)):
    return power_user_repo.fetch_power_user(id, db)
