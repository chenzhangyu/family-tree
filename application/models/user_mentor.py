# encoding=utf8

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from application.models import Base


class UserMentor(Base):

    __tablename__ = "user_mentor"

    mentor_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"),
                       nullable=False, primary_key=True, autoincrement=False)
    mentee_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"),
                       nullable=False, primary_key=True, autoincrement=False)

    mentor = relationship("User", foreign_keys="UserMentor.mentor_id",
                          passive_deletes=True)
    mentee = relationship("User", foreign_keys="UserMentor.mentee_id",
                          passive_deletes=True)
