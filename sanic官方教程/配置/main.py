from sanic import Sanic
from config import db_settings


app = Sanic(__name__)
app.config.from_object(db_settings)
