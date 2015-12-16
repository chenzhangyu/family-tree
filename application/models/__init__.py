# encoding=utf8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.ext.declarative import declarative_base
from tornado.options import options

engine = create_engine(options.db_engine,
                       encoding="utf-8",
                       convert_unicode=True)

Session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()

from application.models.user_activity import user_activity
from application.models.activity import Activity
from application.models.group_relation import GroupRelation
from application.models.user_group import UserGroup
from application.models.group import Group
from application.models.user import User
from application.models.user_mentor import UserMentor
