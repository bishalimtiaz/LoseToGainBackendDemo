from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models import power_user_model
from schemas import power_user_schema
from security.hashing import Hash
from security.jwt_token import create_access_token


def authenticate(request_user: power_user_schema.AuthenticatePowerUser, db: Session):
    power_user = db.query(power_user_model.PowerUser)\
        .filter(power_user_model.PowerUser.email == request_user.email)\
        .first()
    if not power_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(power_user.password, request_user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Wrong Password")
    if not power_user.roles:
        role = "GUEST"
    else:
        role = power_user.roles.user_role.title
    token_payload = {
        "id": str(power_user.id),
        "role": role,
    }
    access_token = create_access_token(
        token_payload
    )
    return {"access_token": access_token, "token_type": "bearer"}
