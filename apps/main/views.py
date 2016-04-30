import tornado.web
import tornado.escape

from sockjs.tornado import SockJSConnection, SockJSRouter



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


