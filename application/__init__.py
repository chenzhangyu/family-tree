# encoding=utf8

import tornado.web

from tornado.options import options

import application.settings  # noqa

from application import fmt


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r"/", fmt.index.IndexHandler),
            (r"/test", fmt.index.TestHandler),
        ]

        application_settings = {
            "debug": options.debug,
            "port": options.port,
            "cookie_secret": options.secret_key,
            "xsrf_cookies": True,
        }

        tornado.web.Application.__init__(self, handlers, **application_settings)
