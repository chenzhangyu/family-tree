# encoding=utf8

from sqlalchemy import Column, Integer, String
from application.models import Base
from sqlalchemy.ext.associationproxy import association_proxy


class Group(Base):

    __tablename__ = "groups"

    group_id = Column(Integer, primary_key=True)
    group_name = Column(String(30), nullable=False)
    start_year = Column(Integer, nullable=False)
    end_year = Column(Integer, nullable=False)
    users = association_proxy("group_users", "user")

    def __init__(self, name, start, end):
        self.group_name = name
        self.start_year = start
        self.end_year = end
