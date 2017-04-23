from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from hedgehog.simple_page import simple_page

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.register_blueprint(simple_page)

db = SQLAlchemy(app)
# This needs to be in the same namespace for migrate to discover
from hedgehog.simple_page import models     # isort:skip
migrate = Migrate(app, db)

from hedgehog.views import *    # isort:skip

