# encoding=utf8

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from application.models import Base


class UserGroup(Base):

    __tablename__ = "usergroup"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    group_id = Column(Integer, ForeignKey("groups.id"), nullable=False)
    year = Column(DateTime, nullable=False)
    user = relationship("User", backref="group_users", cascade="all, delete-orphan")
    group = relationship("Group", backref="user_groups", cascade="all, delete-orphan")
