from sanic import Sanic
from sanic.response import text


app = Sanic(__name__)
'''
路由装饰器接受一个可选的参数，方法，它允许处理程序函数与列表中的任何HTTP方法一起工作
'''
@app.post('/post')
async def post_handler(request):
    return text('POST request - {}'.format(request.json))


@app.get('/get')
async def get_handler(request):
    return text('GET request - {}'.format(request.args))


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)