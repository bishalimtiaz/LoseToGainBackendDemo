from fastapi import APIRouter, Depends, status
from security.oauth2 import get_current_end_user
from schemas import end_user_schema

router = APIRouter(
    prefix='/end_user',
    tags=["Mobile/end_user"]
)


@router.get('/me', response_model=end_user_schema.ShowEndUser, status_code=status.HTTP_200_OK)
def getEndUser(current_user=Depends(get_current_end_user)):
    return current_user
