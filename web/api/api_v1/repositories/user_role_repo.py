from sqlalchemy.orm import Session
from models import user_role_model
from schemas import user_role_schema


def create_user_role(request_user_role: user_role_schema.UserRole, db: Session):
    new_user_role = user_role_model.UserRole(title=request_user_role.title, description=request_user_role.description)
    db.add(new_user_role)
    db.commit()
    db.refresh(new_user_role)
    return new_user_role


def get_user_role(db: Session):
    user_roles = db.query(user_role_model.UserRole).all()
    return user_roles