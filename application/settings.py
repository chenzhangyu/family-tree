# encoding=utf8

from tornado.options import define


define("port", default=23333)
define("debug", default=True)
define("secret_key", default="secret_key")
