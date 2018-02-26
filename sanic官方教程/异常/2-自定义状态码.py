from sanic import Sanic
from sanic.exceptions import abort
from sanic.response import text

'''通过abort可以自定义状态码'''

app = Sanic(__name__)


@app.route('/youshallnotpass')
def no_no(request):
    abort(401)
    # this won't happen 下面的语句不会执行
    text("OK")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
