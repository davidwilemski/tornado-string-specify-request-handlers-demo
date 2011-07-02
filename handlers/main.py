import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, lazy-loaded handlers!")


