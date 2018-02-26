from sanic import Sanic
from sanic.response import text
from sanic import Blueprint

app = Sanic(__name__)

# provide default strict_slashes value for all routes
app = Sanic('test_route_strict_slash', strict_slashes=True)


# you can also overwrite strict_slashes value for specific route
@app.get('/get', strict_slashes=False)
def handler(request):
    return text('OK')


# It also works for blueprints
bp = Blueprint('test_bp_strict_slash', strict_slashes=True)


@bp.get('/bp/get', strict_slashes=False)
def handler(request):
    return text('OK')


app.blueprint(bp)

if __name__ == '__main__':
    app.run()
