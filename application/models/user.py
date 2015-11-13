# encoding=utf8

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from application.models import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    activities = relationship("Activity",
                              secondary="user_activity",
                              backref="users")
