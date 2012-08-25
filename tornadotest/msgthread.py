#-*- coding:utf-8 -*-

import time
import threading

import functools

def lock(f, lock=threading.RLock()):

    @functools.wraps(f)
    def call(*args, **argd):

        with lock:
            
            return f(*args, **argd)

    return call


def init():

    th = threading.Thread(target=run)

    th.setDaemon(True)
    th.start()

    return th


HANDLERS = {}

@lock
def add_handler(handler):

    print 'handler added'

    key = id(handler)

    HANDLERS[key] = handler



@lock
def remove_handler(handler):

    print 'handler removed'

    key = id(handler)

    del HANDLERS[key]


@lock
def map_handlers(f, *args, **argd):

    for v in HANDLERS.values():

        f(v, *args, **argd)
        # v.async_callback(f, *args, **argd)


def run():

    def say_hello(self, *args, **argd):

        print 'say_hello'
        
        self.write_message('yes')


    while 1:    
        map_handlers(say_hello)

        time.sleep(1)

        print 'loop', len(HANDLERS)


    
