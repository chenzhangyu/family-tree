# encoding=utf8

from sqlalchemy import Column, Integer, String, DateTime
from application.models import Base


class Group(Base):

    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    group_name = Column(String(30), nullable=False)
    start_year = Column(DateTime, nullable=False)
    end_year = Column(DateTime, nullable=False)
