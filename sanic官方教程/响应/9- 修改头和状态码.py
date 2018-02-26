from sanic import Sanic
from sanic import response

app = Sanic(__name__)

''' 
修改了请求头和状态码
'''


@app.route('/json')
def handle_request(request):
    return response.json(
        {'message': 'Hello world!'},
        headers={'X-Served-By': 'sanic'},
        status=200
    )


@app.route('/')
def handle_request(request):
    return response.json(
        {'message': 'Hello world!'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
