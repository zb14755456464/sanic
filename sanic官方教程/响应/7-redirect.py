from sanic.response import redirect
from sanic import Sanic
from sanic.response import text

app = Sanic()

'''
redirect 一般和url_for 在一起连用
'''


@app.route('/redirect')
def handle_request(request):
    return redirect('/json')


@app.route('/json')
async def r_json(request):
    return text('json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
