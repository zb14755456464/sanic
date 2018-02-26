from sanic.response import text
from sanic.exceptions import NotFound
from sanic import Sanic

app = Sanic(__name__)


# 只要没找到相应的请求路由，就会执行下面的处理函数
@app.exception(NotFound)
def ignore_404s(request, exception):
    return text("Yep, I totally found the page: {}".format(request.url))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
