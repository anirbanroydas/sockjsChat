# -*- coding: utf-8 -*-
"""
    Simple sockjs-tornado chat application. By default will listen on port 9090.
"""
import tornado.ioloop
import tornado.web
import tornado.escape

from sockjs.tornado import SockJSConnection, SockJSRouter
from multiplex import MultiplexConnection




class IndexHandler(tornado.web.RequestHandler):
    """Regular HTTP handler to serve the chatroom page"""
    def get(self):
        self.render('index.html')
        print


# multiplex.js static handler
class MultiplexStaticHandler(tornado.web.RequestHandler):
    def get(self,f):
    	print "\ninside multiplexerStaticHandler : f  -> ",f
        self.render('multiplex.js')



# Connections
participants=set()

class groupConnection(SockJSConnection):
    def on_open(self, info):
        
	    
		participants.add(self)

    def on_message(self, message):
    	res=tornado.escape.json_decode(message)
    	if res['isFirst']==1:
    		self.broadcast(participants, '***** '+res[name]+' joined *****')
    	else:
        	self.broadcast(participants, '['+res[name]+']  ' + res[message])
 

    def on_close(self):
    	participants.remove(self)
    	self.broadcast(participants,'*** somebody left ***')
	    
	    

	

class privateConnection(SockJSConnection):
    def on_open(self, info):
        self.send('Carl says goodbye!')
        participants.add(self)

    def on_message(self,message):
	    pass

	
    def on_close(self):
	    participants.remove(self)
	    self.broadcast(participants,'Carl Left')



if __name__ == "__main__":
    import logging
    logging.getLogger().setLevel(logging.DEBUG)

    # Create multiplexer
    router = MultiplexConnection.get(group=groupConnection, private=privateConnection)
    print "router : ",router
    # Register multiplexer
    EchoRouter = SockJSRouter(router, '/chat')
    # print "echorouter.ursl : ",EchoRouter.urls
    
    ###
    # Settings
    ###
    settings={
    			# autoreload: If True, the server process will restart when any source files change, as described 
    			'autorlaod':True,
    			# compiled_template_cache: Default is True; 
    			# if False templates will be recompiled on every request.
    			'compiled_template_cache' : False,
    			# serve_traceback: If true, the default error page will include the traceback of the error. 
    			'serve_traceback' : False,
    			# static_hash_cache: Default is True; if False static urls will be recomputed on every request.
    			'static_hash_cache' : False,
    			# static_path: Directory from which static files will be served.
    			'static_path' : os.path.join(PATH,'libs')


    			}

    ##
    # Create application
    #
    
    app = tornado.web.Application(
            [(r"/", IndexHandler), (r"/multiplex.js", MultiplexStaticHandler)] + EchoRouter.urls,
            **settings
    )
    app.listen(9090)

    tornado.ioloop.IOLoop.instance().start()