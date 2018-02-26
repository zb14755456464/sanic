from sanic import Sanic
from myblueprint import bp


app = Sanic(__name__)

'''引入蓝图，进行注册'''

app.blueprint(bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)