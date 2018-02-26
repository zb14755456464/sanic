from sanic.exceptions import ServerError
from sanic import Sanic

'''
异常可以从请求处理程序中抛出，并由Sanic自动处理。异常将消息作为第一个参数，并且还可以将状态代码传回HTTP响应中。
'''
app = Sanic(__name__)


@app.route('/killme')
def i_am_ready_to_die(request):
    raise ServerError("Something bad happened", status_code=500)


# 抛出异常，只需在内部用raise触发即可
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
