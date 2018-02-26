from sanic.response import json
from sanic import Sanic

app = Sanic(__name__)


@app.route("/query_string")
def query_string(request):
    #  http://127.0.0.1:8000/query_string/?a=1&b=2&a=2

    # {"args":{"a":["1"，"2"],"b":["2"]},"url":"http:\/\/0.0.0.0:8000\/query_string\/?a=1&b=2","query_string":"a=1&b=2"}
    return json({"args": request.args, "url": request.url, "query_string": request.query_string})


if __name__ == '__main__':
    app.run()
