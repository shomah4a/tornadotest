#-*- coding:utf-8 -*-
u'''
てすとちゅう
'''

import sys
import os


__version__ = '0.1.0'
__author__ = '@shomah4a'

__license__ = 'GPLv2'



def main(args):

    from tornado import ioloop, web, websocket

    import serve
    import msgthread

    th = msgthread.init()

    app = web.Application([
            ('/', serve.MainHandler),
            ('/websock', serve.OnWebsock),
            ('/yes', serve.YesHandler),
            ('/print/(?P<aaa>.*)', serve.PrintHandler),
            ])
    app.listen(8000)
    ioloop.IOLoop.instance().start()


