from sanic import Sanic
from sanic.response import text

app = Sanic(__name__)

'''
为参数指定类型，在参数名后面添加（：类型）。如果参数不匹配指定的类型，
Sanic将抛出一个不存在的异常，导致一个404页面
'''


@app.route('/number/<integer_arg:int>')
async def integer_handler(request, integer_arg):
    return text('Integer - {}'.format(integer_arg))


@app.route('/number/<number_arg:number>')
async def number_handler(request, number_arg):
    return text('Number - {}'.format(number_arg))


@app.route('/person/<name:[A-z]+>')
async def person_handler(request, name):
    return text('Person - {}'.format(name))


@app.route('/folder/<folder_id:[A-z0-9]{0,4}>')
async def folder_handler(request, folder_id):
    return text('Folder - {}'.format(folder_id))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
