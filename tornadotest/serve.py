#-*- coding:utf-8 -*-

import pprint

from tornado import ioloop, web, websocket

import msgthread


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



import pprint
        

class PrintHandler(web.RequestHandler):

    def get(self, *args, **argd):
        u'''
        :param *args: URL マッピング時の名前なしグルーピング
        :param **argd: URL マッピング時の名前付きグルーピング

        レスポンスボディは self.write で書き込んでやる。
        '''

        # レスポンスヘッダを弄る
        self.set_header('Content-Type', 'text/plain;charset=utf-8')

        print >> self, args, argd

        # URL パラメータから値を一個取る
        print >> self, self.get_argument('aaa')

        # URL パラメータから値を全部取る
        print >> self, self.get_arguments('aaa')

        # self.request がリクエストオブジェクト
        # リクエストオブジェクトの arguments にパラメータが辞書で入っている
        pprint.pprint(self.request.arguments, stream=self)

