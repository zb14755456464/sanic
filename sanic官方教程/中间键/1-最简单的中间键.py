from sanic import Sanic
from sanic.response import text

app = Sanic(__name__)

'''
最简单的中间件根本不修改请求或响应
'''


@app.middleware('request')
async def print_on_request(request):
    print("I print when a request is received by the server")


@app.middleware('response')
async def print_on_response(request, response):
    print("I print when a response is returned by the server")


@app.route('/')
async def index(request):
    return text('hello world')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
