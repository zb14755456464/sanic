from sanic import Sanic
app = Sanic(__name__)


'''根据输入的路径在静态文件下找相应的文件'''
# Serves files from the static folder to the URL /static
app.static('/static', './static')



'''根据输入的路径，绑定静态的文件'''
# Serves the file /home/ubuntu/test.png when the URL /the_best.png
# is requested
app.static('/whatever', './static/whatever.png')

if __name__ == '__main__':


    app.run(host="0.0.0.0", port=8000)