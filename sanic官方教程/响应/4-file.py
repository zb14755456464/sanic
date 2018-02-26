from sanic import response
from sanic import Sanic
app = Sanic()

'''
返回的是一个文件的类型
'''


@app.route('/file')
async def handle_request(request):
    return await response.file('./whatever.png')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)