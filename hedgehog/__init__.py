from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from hedgehog.simple_page import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)

db = SQLAlchemy(app)

from hedgehog.views import *    # isort:skip

