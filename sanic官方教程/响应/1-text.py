from sanic import Sanic
from sanic import response

app = Sanic(__name__)

# 返回的是纯文本
@app.route('/text')
def handle_request(request):
    return response.text('Hello world!')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
