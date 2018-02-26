from sanic import Sanic
import jwt
from functools import wraps
from sanic.views import HTTPMethodView
from sanic.response import text

app = Sanic(__name__)


def authorized():
    def decorator(f):
        @wraps(f)
        async def decorated_function(self, request, *args, **kwargs):
            token = request.cookies.get('token')
            if token:
                decoded = jwt.decode(token, 'secret', algorithms='HS256')
                if decoded['some'] == 'payload':
                    response = await f(self, request, *args, **kwargs)
                    return response
            else:
                return text('请登录后在访问')

        return decorated_function

    return decorator


class SimpView(HTTPMethodView):
    @authorized()
    async def get(self, request):
        return text('I am get method')

    async def post(self, request):
        return text('I am post method')


@app.route("/login")
async def login(request):
    response = text('登录成功')
    encode = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')
    response.cookies['token'] = encode.decode()
    return response


app.add_route(SimpView.as_view(), '/')

if __name__ == '__main__':
    app.run()
