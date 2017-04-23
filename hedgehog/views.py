from hedgehog import app

@app.route('/')
def index():
  return "hello"
