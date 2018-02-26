from sanic import Sanic
from sanic.response import text

app = Sanic(__name__)


@app.route('/tag/<tag>')
async def tag_handler(request, tag):
    return text(tag)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
