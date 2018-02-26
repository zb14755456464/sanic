from sanic import Sanic
from sanic.response import text

app = Sanic(__name__)

'''
中间件可以修改它所提供的请求或响应参数，下面的都依次进行执行了
'''


@app.middleware('response')
async def custom_banner(request, response):
    response.headers["Server"] = "Fake-Server"


@app.middleware('response')
async def prevent_xss(request, response):
    response.headers["x-xss-protection"] = "1; mode=block"


@app.route('/')
async def index(request):
    return text('hello world')


'''
上述代码将按顺序应用这两个中间件。首先，中间件custom_banner将把HTTP响应头服务器更改为假服务器，
而第二个中间件防止XSS将添加HTTP头来防止跨站点脚本攻击(XSS)攻击。这两个函数是在用户函数返回响应之后调用的。

'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
