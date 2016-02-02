# encoding=utf8

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from application.models import Base


class GroupRelation(Base):

    __tablename__ = "group_relation"

    group_from_id = Column(Integer,
                           ForeignKey("groups.group_id", ondelete="CASCADE"),
                           nullable=False, primary_key=True,
                           autoincrement=False)
    group_to_id = Column(Integer,
                         ForeignKey("groups.group_id", ondelete="CASCADE"),
                         nullable=False, primary_key=True,
                         autoincrement=False)

    group_from = relationship("Group",
                              foreign_keys="GroupRelation.group_from_id",
                              passive_deletes=True)
    group_to = relationship("Group",
                            foreign_keys="GroupRelation.group_to_id",
                            passive_deletes=True)
