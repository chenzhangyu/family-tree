# encoding=utf8

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from application.models import Base


class UserMentor(Base):

    __tablename__ = "user_mentor"

    id = Column(Integer, primary_key=True)

    mentor_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    mentee_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    mentor = relationship("User", foreign_keys="UserMentor.mentor_id", passive_deletes=True)
    mentee = relationship("User", foreign_keys="UserMentor.mentee_id", passive_deletes=True)
