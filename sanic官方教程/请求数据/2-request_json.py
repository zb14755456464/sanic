from sanic.response import json
from sanic import Sanic

app = Sanic(__name__)


# 通过postman
@app.post("/json")
def post_json(request):
    return json({"received": True, "message": request.json})


if __name__ == '__main__':
    app.run()
