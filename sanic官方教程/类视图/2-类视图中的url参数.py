from sanic import Sanic
from sanic.response import text
from sanic.views import HTTPMethodView

app = Sanic(__name__)


# 在类视图中，接受url地址栏中的参数

class NameView(HTTPMethodView):
    def get(self, request, name):
        return text('Hello {}'.format(name))


app.add_route(NameView.as_view(), '/<name>')

if __name__ == '__main__':
    app.run()