from sanic.response import text
from sanic.exceptions import ServerError
from sanic import Sanic

app = Sanic(__name__)
'''ServerError:当服务器内部出现问题时调用。如果在用户代码中出现异常，通常会出现这种情况'''


@app.exception(ServerError)
def ignore_404s(request, exception):
    return text("Yep, I totally found the page: {}".format(request.url))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)