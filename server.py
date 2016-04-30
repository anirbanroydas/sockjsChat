# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

from sockjs.tornado import SockJSConnection, SockJSRouter
from multiplex import MultiplexConnection


# Index page handler
class IndexHandler(tornado.web.RequestHandler):
    """Regular HTTP handler to serve the chatroom page"""
    def get(self):
        self.render('index.html')


# multiplex.js static handler
class MultiplexStaticHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('multiplex.js')


# Connections
participants=set()

class AnnConnection(SockJSConnection):
    def on_open(self, info):
        self.send('Ann says hi!!')
	participants.add(self)

    def on_message(self, message):
        self.broadcast(participants,'Ann : ' + message)
 



  


class BobConnection(SockJSConnection):
    def on_open(self, info):
        self.send('Bob doesn\'t agree.')
	participants.add(self)

    def on_message(self, message):
        self.broadcast(participants,'Bob : ' + message)
	

class CarlConnection(SockJSConnection):
    def on_open(self, info):
        self.send('Carl says goodbye!')
	participants.add(self)

        self.close()

    def on_message(self,message):
	    pass

	
    def on_close(self):
	    participants.remove(self)
	    self.broadcast(participants,'Carl Left')

if __name__ == "__main__":
    import logging
    logging.getLogger().setLevel(logging.DEBUG)

    # Create multiplexer
    router = MultiplexConnection.get(ann=AnnConnection, bob=BobConnection, carl=CarlConnection)
    print "router : ",router
    # Register multiplexer
    EchoRouter = SockJSRouter(router, '/echo')
    # print "echorouter.ursl : ",EchoRouter.urls
    # Create application
    app = tornado.web.Application(
            [(r"/", IndexHandler), (r"/multiplex.js", MultiplexStaticHandler)] + EchoRouter.urls
    )
    app.listen(9999)

    tornado.ioloop.IOLoop.instance().start()
