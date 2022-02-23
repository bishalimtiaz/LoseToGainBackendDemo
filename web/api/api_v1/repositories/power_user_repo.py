from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from schemas import power_user_schema
from models import power_user_model
from security.hashing import Hash


# Create Power User
def create_power_user(user_role: power_user_schema.CreatePowerUser, db: Session):
    new_power_user = power_user_model.PowerUser(
        user_name=user_role.user_name,
        email=user_role.email,
        password=Hash.encrypt(user_role.password))
    db.add(new_power_user)
    db.commit()
    db.refresh(new_power_user)
    return new_power_user


# get blog with id
def fetch_power_user(id, db: Session):
    power_user = db.query(power_user_model.PowerUser).filter(power_user_model.PowerUser.id == id).first()
    print(power_user.roles.user_role.title)
    if not power_user:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'message': f"Blog with id {id} not available"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")
    return power_user
