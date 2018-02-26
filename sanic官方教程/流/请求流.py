from sanic import Sanic
from sanic.views import CompositionView
from sanic.views import HTTPMethodView
from sanic.views import stream as stream_decorator
from sanic.blueprints import Blueprint
from sanic.response import stream, text

bp = Blueprint('blueprint_request_stream')
app = Sanic('request_stream')

'''
Sanic允许通过流获得请求数据，如下所示。
当请求结束时，request.stream.get()返回None。只有post、put和补丁修饰器才有流参数。
'''

class SimpleView(HTTPMethodView):
    @stream_decorator
    async def post(self, request):
        result = ''
        while True:
            body = await request.stream.get()
            if body is None:
                break
            result += body.decode('utf-8')
        return text(result)


@app.post('/stream', stream=True)
async def handler(request):
    async def streaming(response):
        while True:
            body = await request.stream.get()
            if body is None:
                break
            body = body.decode('utf-8').replace('1', 'A')
            response.write(body)

    return stream(streaming)


@bp.put('/bp_stream', stream=True)
async def bp_handler(request):
    result = ''
    while True:
        body = await request.stream.get()
        if body is None:
            break
        result += body.decode('utf-8').replace('1', 'A')
    return text(result)


async def post_handler(request):
    result = ''
    while True:
        body = await request.stream.get()
        if body is None:
            break
        result += body.decode('utf-8')
    return text(result)


app.blueprint(bp)
app.add_route(SimpleView.as_view(), '/method_view')

view = CompositionView()
view.add(['POST'], post_handler, stream=True)
app.add_route(view, '/composition_view')
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
