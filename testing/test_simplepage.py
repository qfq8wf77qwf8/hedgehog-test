import unittest

from hedgehog import app, db
from hedgehog.config import TestingConfig


class SimplePageTestCase(unittest.TestCase):

  def setUp(self):
    self.app = app
    self.app.config['TESTING'] = True
    self.app.config.from_object(TestingConfig)
    self.app_context = self.app.app_context()
    self.client = app.test_client()

    self.app_context.push()
    db.create_all()

  def tearDown(self):
    db.session.remove()
    db.drop_all()
    self.app_context.pop()

  def test_simple(self):
    r = self.client.get('/simple_page/')
    assert "Hello from simple_page/__init__.py" in r.data

