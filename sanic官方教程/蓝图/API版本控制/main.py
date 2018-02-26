from sanic import Sanic
from blueprints import blueprint_v1, blueprint_v2


app = Sanic(__name__)
app.blueprint(blueprint_v1, url_prefix='/v1')
app.blueprint(blueprint_v2, url_prefix='/v2')





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
