from sanic import Sanic
from sanic.response import text, json
from sanic.views import HTTPMethodView

app = Sanic(__name__)


# 在类视图中，添加装饰器
def authorized(*args):
    def decorator(f):
        async def decorated_function(request, *args, **kwargs):

            is_authorized = True

            if is_authorized:
                # the user is authorized.
                # run the handler method and return the response
                response = await f(request, *args, **kwargs)
                return response
            else:
                return json({'status': 'not_authorized'})

        return decorated_function

    if args:
        return decorator(*args)
    else:
        return decorator


def pro(*args):
    def decorator(f):
        async def decorated_function(request, *args, **kwargs):

            is_authorized = False

            if is_authorized:
                # the user is authorized.
                # run the handler method and return the response
                response = await f(request, *args, **kwargs)
                return response
            else:
                return json({'status': 'pro not auth success'})

        return decorated_function

    if args:
        return decorator(*args)
    else:
        return decorator


class ViewWithDecorator(HTTPMethodView):
    decorators = [authorized, pro]

    async def get(self, request):
        return text('Hello I have a decorator')

    async def post(self, request):
        return text('Hello I have a decorator')


app.add_route(ViewWithDecorator.as_view(), '/')

if __name__ == '__main__':
    app.run()
