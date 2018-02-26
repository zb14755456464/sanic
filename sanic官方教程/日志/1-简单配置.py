from sanic import Sanic, config
from sanic import response

app = Sanic('test', log_config=config)


@app.route('/')
async def test(request):
    return response.text('Hello World!')


if __name__ == "__main__":
    app.run(debug=True, access_log=True)
