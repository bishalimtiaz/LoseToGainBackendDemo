from pydantic import BaseModel


class PowerUserBase(BaseModel):
    user_name: str
    email: str


class CreatePowerUser(PowerUserBase):
    password: str

    class Config:
        orm_mode = True


class ShowPowerUser(PowerUserBase):

    class Config:
        orm_mode = True


class AuthenticatePowerUser(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True
