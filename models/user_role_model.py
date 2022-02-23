from sqlalchemy import Column, String, Integer, TEXT

from models.meta import Base


class UserRole(Base):
    __tablename__ = "user_role"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(16))
    description = Column(TEXT)
