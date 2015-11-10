# encoding=utf8

from application.baseview import BaseHandler


class IndexHandler(BaseHandler):

    def get(self):
        self.set_secure_cookie("name", "lance")
        self.write("index")


class TestHandler(BaseHandler):

    def get(self):
        name = self.get_secure_cookie("name")
        print name
        self.write("test")
