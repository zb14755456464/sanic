from sanic import Sanic
from sanic.response import text
from sanic.response import redirect
import jwt


app = Sanic(__name__)

'''
Cookies是在用户的浏览器内持续存在的数据片段。Sanic可以读取和写入存储为键值对的cookie。
'''

@app.route("/login")
async def login(request):
    response = text('登录成功')
    encode = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')
    response.cookies['token'] = encode.decode()
    return response

# 读取cookies，用户的cookies可以通过Request对象的cookies字典访问。
@app.route("/pass")
async def test(request):
    token = request.cookies.get('token')
    print(token)
    if token:
        decoded = jwt.decode(token, 'secret', algorithms='HS256')
        if decoded['some'] == 'payload':
            return text("Test Token set is: {}".format(token))
    else:
        return text('请登录后在访问')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)