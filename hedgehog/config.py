import os


class TestingConfig(object):
  SERVER_NAME = 'Testing'
  DEBUG = True
  TESTING = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(object):
  DEBUG = True
  TESTING = False
  SECRET_KEY = 'some_secret_key'
  SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/hedgehog'


class HerokuConfig(DevelopmentConfig):
  DEBUG = False
  TESTING = False
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', None)
