from sanic import response
from sanic import Sanic
app = Sanic()


@app.route('/html')
def handle_request(request):
    return response.html('<h1>Hello world!</h1>')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)