# encoding=utf8

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from application.models import Base


class InvCode(Base):

    __tablename__ = "inv_code"

    inv_id = Column(Integer, primary_key=True)
    code = Column(String(32), nullable=False, unique=True)
    is_used = Column(Boolean, nullable=False, default=False)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"))

    def __init__(self, code, is_used=False, user_id=None):
        self.code = code
        self.is_used = is_used
        self.user_id = user_id
