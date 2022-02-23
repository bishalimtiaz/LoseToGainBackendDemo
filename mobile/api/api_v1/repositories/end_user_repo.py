from sqlalchemy.orm import Session
from models import end_user_model


def get_end_user(db: Session, id: str, auth_user_id: str):
    return db.query(end_user_model.EndUser)\
        .filter(end_user_model.EndUser.id == id, end_user_model.EndUser.auth_user_id == auth_user_id)\
        .first()
