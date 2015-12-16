# encoding=utf8

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from application.models import Base


class GroupRelation(Base):

    __tablename__ = "group_relation"

    id = Column(Integer, primary_key=True)

    group_from_id = Column(Integer, ForeignKey("groups.id", ondelete="CASCADE"), nullable=False)
    group_to_id = Column(Integer, ForeignKey("groups.id", ondelete="CASCADE"), nullable=False)

    group_from = relationship("Group", foreign_keys="GroupRelation.group_from_id", passive_deletes=True)
    group_to = relationship("Group", foreign_keys="GroupRelation.group_to_id", passive_deletes=True)
