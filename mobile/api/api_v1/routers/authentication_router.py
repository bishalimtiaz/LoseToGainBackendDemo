from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from security.database import get_db
from mobile.api.api_v1.repositories import authentication_repo

router = APIRouter(
    prefix='/auth',
    tags=["Mobile/auth"]
)


@router.post('/google_login')
def googleLogin(access_token: str,  response: Response, db: Session = Depends(get_db)):
    return authentication_repo.googleLogin(access_token, db, response)


@router.post('/fb_login')
def facebookLogin(access_token: str,  response: Response, db: Session = Depends(get_db)):
    return authentication_repo.facebookLogin(access_token, db, response)
