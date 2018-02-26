from sanic import Sanic
from sanic.response import redirect,text

app = Sanic(__name__)

'''

Sanic提供了一个url_for方法，根据处理程序方法名生成url。避免硬编码url路径到您的应用程序

'''

@app.route('/')
async def index(request):
    # generate a URL for the endpoint `post_handler`
    # url = app.url_for('post_handler', post_id=5)

    # http://0.0.0.0:8000/posts/5?arg_one=one&arg_two=two
    url = app.url_for('post_handler', post_id=5, arg_one='one', arg_two='two')

    # http://0.0.0.0:8000/posts/5?arg_one=one&arg_one=two
    # url = app.url_for('post_handler', post_id=5, arg_one=['one', 'two'])

    # the URL is `/posts/5`, redirect to it
    return redirect(url)


@app.route('/posts/<post_id>')
async def post_handler(request, post_id):
    return text('Post - {}'.format(post_id))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)