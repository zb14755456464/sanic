from sanic import response
from sanic import Sanic
app = Sanic(__name__)

'''
这个需要强行的记忆，返回的是一个json的数据
'''


@app.route('/json')
def handle_request(request):
    return response.json({'message': 'Hello world!'})


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)