#-*- coding:utf-8 -*-
u'''
てすとちゅう
'''

import sys
import os
import pprint

from tornado import ioloop, web, websocket

import msgthread

__version__ = '0.1.0'
__author__ = '@shomah4a'

__license__ = 'GPLv2'



class MainHandler(web.RequestHandler):

    def get(self):
        
        pprint.pprint(dir(self))

        self.write('hello, tornado')



class OnWebsock(web.RequestHandler):

    def get(self):

        print >> self, u'''
<html>
<head>
<script type="text/javascript">
var ws = new WebSocket("ws://localhost:8000/yes");
ws.onopen = function() {
  ws.send("Hello, world");
};
ws.onmessage = function (evt) {
  document.write(evt.data);
  document.write('<br/>');
};
ws.onclose = function (evt) {
  document.write('closed');
};

</script>
</head>
<body>
aaa
</body>
</html>
'''


class YesHandler(websocket.WebSocketHandler):

    def open(self):

        print 'open'
        self.count = 0

        msgthread.add_handler(self)


    def on_message(self, evt):

        print 'aaaaa'
        print evt

        self.write_message('yes'+str(self.count))
        self.count += 1


    def on_close(self):

        print 'close'

        msgthread.remove_handler(self)
        


def main(args):

    th = msgthread.init()

    app = web.Application([
            ('/', MainHandler),
            ('/websock', OnWebsock),
            ('/yes', YesHandler),
            ])
    app.listen(8000)
    ioloop.IOLoop.instance().start()


