# encoding=utf8

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.schema import Table
from application.models import Base


user_activity = Table("user_activity", Base.metadata,
                      Column("user_id", Integer,
                             ForeignKey("users.id", ondelete="CASCADE"),
                             nullable=False),
                      Column("activity_id", Integer,
                             ForeignKey("activity.id", ondelete="CASCADE"),
                             nullable=False))
