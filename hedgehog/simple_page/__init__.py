from flask import Blueprint

simple_page = Blueprint('simple_page', __name__, url_prefix='/simple_page')

@simple_page.route('/')
def hello():
  return "Hello from simple_page/__init__.py"

