from sanic import Sanic
from sanic.server import HttpProtocol
from sanic.response import text

app = Sanic(__name__)


class CustomHttpProtocol(HttpProtocol):
    def __init__(self, *, loop, request_handler, error_handler,
                 signal, connections, request_timeout, request_max_size):
        super().__init__(
            loop=loop, request_handler=request_handler,
            error_handler=error_handler, signal=signal,
            connections=connections, request_timeout=request_timeout,
            request_max_size=request_max_size)

    def write_response(self, response):
        if isinstance(response, str):
            response = text(response)
        self.transport.write(
            response.output(self.request.version)
        )
        self.transport.close()


@app.route('/')
async def string(request):
    return 'string'


@app.route('/1')
async def response(request):
    return text('response')


app.run(host='0.0.0.0', port=8000, protocol=CustomHttpProtocol)
