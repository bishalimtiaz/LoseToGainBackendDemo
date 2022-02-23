from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from schemas import power_user_permission_schema
from models import power_user_permission_model


def create_power_user_permission(power_user_permission: power_user_permission_schema.PowerUserPermissionBase, db):
    new_power_user_permission = power_user_permission_model.PowerUserPermission(
        power_user_id=power_user_permission.power_user_id,
        user_role_id=power_user_permission.user_role_id
    )
    db.add(new_power_user_permission)
    db.commit()
    db.refresh(new_power_user_permission)
    return new_power_user_permission


def fetch_Permissions(id, db: Session):
    permission = db.query(power_user_permission_model.PowerUserPermission) \
        .filter(power_user_permission_model.PowerUserPermission.id == id).first()
    if not permission:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'message': f"Blog with id {id} not available"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Permission with id {id} not found")
    return permission
