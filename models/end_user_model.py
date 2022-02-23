import datetime

from sqlalchemy import Column, String, TEXT, Boolean, DateTime


from models.meta import Base


class EndUser(Base):
    __tablename__ = "end_user"

    id = Column(String(40), primary_key=True, nullable=False)
    auth_user_id = Column(String(32))
    user_name = Column(String(32))
    email = Column(TEXT)
    profile_pic = Column(TEXT)
    auth_provider = Column(String(8))
    is_active = Column(Boolean, default=True)
    is_premium = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.datetime.utcnow(), onupdate=datetime.datetime.utcnow())
