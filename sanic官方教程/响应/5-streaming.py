from sanic import Sanic
from sanic import response


app = Sanic()


@app.route("/streaming")
async def index(request):
    async def streaming_fn(response):
        response.write('foo')
        response.write('bar')
        response.write('bar')
        #  foobarbar  可以在一起进行拼接

    return response.stream(streaming_fn, content_type='text/plain')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
