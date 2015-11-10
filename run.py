# encoding=utf8

import tornado.options
import tornado.ioloop

from application import Application
import application.settings


def main():
    tornado.options.parse_command_line()
    application = Application()
    application.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
