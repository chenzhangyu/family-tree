# encoding=utf8

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from application.models import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    activities = relationship("Activity",
                              secondary="user_activity",
                              backref="users",
                              passive_deletes=True)
    groups = association_proxy("user_groups", "group")

    def __init__(self, name):
        self.username = name
