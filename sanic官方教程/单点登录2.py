from sanic import Sanic
from sanic.response import text, json
from sanic.response import redirect
import jwt
from functools import wraps

app = Sanic(__name__)


def authorized():
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            token = request.cookies.get('token')
            if token:
                decoded = jwt.decode(token, 'secret', algorithms='HS256')
                if decoded['some'] == 'payload':
                    response = await f(request, *args, **kwargs)
                    return response
            else:
                return text('请登录后在访问')

        return decorated_function

    return decorator


@app.route("/login")
async def login(request):
    response = text('登录成功')
    encode = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')
    response.cookies['token'] = encode.decode()
    return response


@app.route('cart')
@authorized()
async def cart(request):
    return text('cart')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
