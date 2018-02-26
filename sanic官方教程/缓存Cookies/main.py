from sanic import Sanic
from sanic.response import text
from sanic.response import redirect
import datetime

app = Sanic(__name__)

'''
Cookies是在用户的浏览器内持续存在的数据片段。Sanic可以读取和写入存储为键值对的cookie。
'''


@app.route("/login")
async def login(request):
    return text('登录成功')


# 读取cookies，用户的cookies可以通过Request对象的cookies字典访问。
@app.route("/get_cookie")
async def test(request):
    token = request.cookies.get('token')

    return text("Test Token set is: {}".format(token))


# 在返回响应时，可以在Response对象上设置Cookie 。
@app.route("/set_cookie")
async def test(request):
    response = text("There's a cookie up in this response")
    response.cookies['token'] = 'It worked!'
    date = datetime.datetime.now()
    response.cookies['token']['expires'] = date + datetime.timedelta(days=30)
    response.cookies['token']['httponly'] = True
    return response


# 可以在语义上或明确地删除Cookie。
@app.route("/del_cookie")
async def test(request):
    response = text("Time to eat some cookies muahaha")

    # This cookie will be set to expire in 0 seconds
    del response.cookies['test']
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
