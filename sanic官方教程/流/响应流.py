from sanic import Sanic
from sanic.response import stream
import asyncpg
from sanic import Sanic
from sanic.response import stream

app = Sanic(__name__)

'''
Sanic允许使用流方法将内容流到客户端。该方法接受一个coroutine回调，
该回调被传递给了一个被写入的StreamingHTTPResponse对象。一个简单的例子如下:
'''


@app.route("/")
async def test(request):
    async def sample_streaming_fn(response):
        response.write('foo,')
        response.write('bar')

    return stream(sample_streaming_fn, content_type='text/csv')


'''
当希望将内容流到源自外部服务的客户端，比如数据库时，这一点非常有用。
例如，您可以使用asyncpg提供的异步光标将数据库记录流到客户端:
'''


@app.route("/index")
async def index(request):
    async def stream_from_db(response):
        conn = await asyncpg.connect(database='test')
        async with conn.transaction():
            async for record in conn.cursor('SELECT generate_series(0, 10)'):
                response.write(record[0])

    return stream(stream_from_db)


if __name__ == '__main__':
    app.run()
