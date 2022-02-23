from pydantic import BaseModel
from schemas import user_role_schema, power_user_schema


class PowerUserPermissionBase(BaseModel):
    power_user_id: int
    user_role_id: int


class CreatePowerUserPermission(PowerUserPermissionBase):
    pass


class ShowPowerUserPermission(PowerUserPermissionBase):
    user_role: user_role_schema.UserRole
    user_permission: power_user_schema.ShowPowerUser

    class Config:
        orm_mode = True
