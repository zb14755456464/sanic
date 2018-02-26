from sanic import Sanic
from sanic.views import HTTPMethodView
from sanic.response import text

app = Sanic('some_name')


# 必须继承 HTTPMethodView 类
# 添加到 app._route(类视图.as_view(),'/url')
class SimpView(HTTPMethodView):
    def get(self, request):
        return text('I am get method')

    def post(self, request):
        return text('I am post method')

    def put(self, request):
        return text('I am put method')

    def patch(self, request):
        return text('I am patch method')

    def delete(self, request):
        return text('I am delete method')


app.add_route(SimpView.as_view(), '/')

if __name__ == '__main__':
    app.run()