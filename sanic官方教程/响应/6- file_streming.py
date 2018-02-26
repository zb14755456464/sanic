from sanic import response
from sanic import Sanic
from sanic import response

app = Sanic()

# 对于一个大文件，可以使用文件和流的组合
@app.route("/big_file.png")
async def index(request):
    return await response.file_stream('./whatever.png')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
