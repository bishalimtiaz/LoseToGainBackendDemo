from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.meta import Base


class PowerUserPermission(Base):
    __tablename__ = "power_user_permission"

    id = Column(Integer, primary_key=True, index=True)
    power_user_id = Column(Integer, ForeignKey('power_user.id'))
    user_role_id = Column(Integer, ForeignKey('user_role.id'))
    user_role = relationship("UserRole")
    user_permission = relationship("PowerUser", back_populates="roles")
