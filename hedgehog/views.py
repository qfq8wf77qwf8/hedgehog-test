from hedgehog import app


@app.route('/')
def index():
  return "hello from hedgehog/__init__.py"
