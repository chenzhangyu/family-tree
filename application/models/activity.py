# encoding=utf8

from sqlalchemy import Column, Integer, String, DateTime
from application.models import Base


class Activity(Base):

    __tablename__ = "activity"

    id = Column(Integer, primary_key=True)
    description = Column(String(300), nullable=False)
    year = Column(DateTime, nullable=False)
