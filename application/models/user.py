# encoding=utf8

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

from application.models import Base


class User(Base):

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False)
    password = Column(String(50), nullable=False)
    avatar = Column(String(50), nullable=False, default="")
    blog = Column(String(50))
    wechat_id = Column(String(50))
    location = Column(String(50))
    is_gratuated = Column(Boolean, nullable=False, default=False)
    activities = relationship("Activity",
                              secondary="user_activity",
                              backref="users",
                              passive_deletes=True)
    groups = association_proxy("user_groups", "group")

    def __init__(self, name, email=email):
        self.username = name
        self.email = email
