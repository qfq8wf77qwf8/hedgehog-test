from flask import Flask

from hedgehog.simple_page import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)

from hedgehog.views import *    # isort:skip

