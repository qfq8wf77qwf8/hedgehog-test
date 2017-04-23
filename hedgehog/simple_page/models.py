from hedgehog import db


class Page(db.Model):
  id = db.Column(db.Integer, primary_key=True)

