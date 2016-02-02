# encoding=utf8

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from application.models import Base


class UserGroup(Base):

    __tablename__ = "user_group"

    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"),
                     nullable=False, primary_key=True, autoincrement=False)
    group_id = Column(Integer, ForeignKey("groups.group_id", ondelete="CASCADE"),
                      nullable=False, primary_key=True, autoincrement=False)
    year = Column(Integer, nullable=False,
                  primary_key=True, autoincrement=False)

    user = relationship("User",
                        backref=backref("user_groups", passive_deletes=True))
    group = relationship("Group",
                         backref=backref("group_users", passive_deletes=True))

    def __init__(self, year, g, u):
        self.user = u
        self.group = g
        self.year = year
