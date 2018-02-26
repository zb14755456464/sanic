from sanic.response import text
from sanic import Blueprint
from sanic.response import redirect

blueprint_v1 = Blueprint('v1', url_prefix='/v1')
blueprint_v2 = Blueprint('v2', url_prefix='/v2')


@blueprint_v1.route('/')
async def api_v1_root(request):
    return text('Welcome to version 1 of our documentation')


@blueprint_v2.route('/')
async def api_v2_root(request):
    return text('Welcome to version 2 of our documentation')


'''
如果希望在blueprint内部路由生成一个URL，记住，端点名称采用格式<blueprint_name>.<handler_name>
'''


@blueprint_v1.route('/url_for')
async def root(request):
    from main import app
    url = app.url_for('v1.post_handler', post_id=5)  # --> '/v1/post/5'
    return redirect(url)


@blueprint_v1.route('/post/<post_id>')
async def post_handler(request, post_id):
    return text('Post {} in Blueprint V1'.format(post_id))
