from pydantic import BaseModel


class EndUserBase(BaseModel):
    user_name: str
    email: str
    profile_pic: str


class ShowEndUser(EndUserBase):
    class Config:
        orm_mode = True
