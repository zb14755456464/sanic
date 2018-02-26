from sanic.response import json
from sanic import Blueprint

'''稍后可以导入到您的主应用程序中'''
bp = Blueprint('my_blueprint')

# 可以为蓝图指定静态文件
bp.static('/static', './static')


@bp.route('/')
async def bp_root(request):
    return json({'my': 'blueprint'})
