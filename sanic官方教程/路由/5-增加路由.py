from sanic import Sanic
from sanic.response import text

app = Sanic(__name__)

'''
这个就是在定义好函数后，给他添加路由到指定的函数中
'''
# Define the handler functions
async def handler1(request):
    return text('OK')


async def handler2(request, name):
    return text('Folder - {}'.format(name))


async def person_handler2(request, name):
    return text('Person - {}'.format(name))


# Add each handler function as a route
app.add_route(handler1, '/test')
app.add_route(handler2, '/folder/<name>')
app.add_route(person_handler2, '/person/<name:[A-z]>', methods=['GET'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
