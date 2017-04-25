
import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from hedgehog.config import DevelopmentConfig, HerokuConfig
from hedgehog.simple_page import simple_page

"""
The following variable exist here:
- app
- db

This allows us to do `from hedgehog import app, db`, as long
as we install this package properly via `pip install -e`
"""

app = Flask(__name__)
app.register_blueprint(simple_page)

if os.environ.get('HEROKU', False):
  app.config.from_object(HerokuConfig)
else:
  app.config.from_object(DevelopmentConfig)


db = SQLAlchemy(app)
# This needs to be in the same namespace for migrate to discover
from hedgehog.simple_page import models     # isort:skip
migrate = Migrate(app, db)

from hedgehog.views import *    # isort:skip
