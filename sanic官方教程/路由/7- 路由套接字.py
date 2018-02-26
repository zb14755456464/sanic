from sanic import Sanic
from sanic.response import text


app = Sanic(__name__)


@app.websocket('/feed')
async def feed(request, ws):
    while True:
        data = 'hello!'
        print('Sending: ' + data)
        await ws.send(data)
        data = await ws.recv()
        print('Received: ' + data)


#  另外一种添加路由的方法

async def feed_one(request, ws):
    pass

app.add_websocket_route(feed_one, '/f')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)