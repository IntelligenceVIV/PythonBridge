# @Time    : 2019/4/18 2:48
# @Author  : Noah
# @File    : tornado_demo.py
# @Software: PyCharm
# @description: simple tornado
import tornado.web
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("Hello tornado")


def make_app():
    return tornado.web.Application([
        ('/', MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
