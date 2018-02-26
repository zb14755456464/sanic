from sanic import Sanic
from sanic import response

app = Sanic(__name__)


@app.route('/raw')
def handle_request(request):
    return response.raw(b'raw data')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
