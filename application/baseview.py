# encoding=utf8

import tornado.web
from application.models import Session


class BaseHandler(tornado.web.RequestHandler):

    def prepare(self):
        self.db_session = Session()

    def on_finish(self):
        self.db_session.remove()

    def get_current_user(self):
        pass
