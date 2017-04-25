
import logging
import os
import subprocess

import coloredlogs
from flask_script import Manager

from hedgehog import app

manager = Manager(app)

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)


@manager.command
def install():
  """Installs this pacakge for the first time.
  """
  subprocess.check_output(['pip', 'install', '-e', '.'])


@manager.command
def freeze():
  """`pip freeze` and patches the line from installing this package.

  Pip freeze is causing an issue for this package that is installed
  locally through `pip install -e`.
  """
  out = subprocess.check_output(['pip', 'freeze'])
  l = out.split('\n')

  replace_i = 0
  for i, package in enumerate(l):
    if package.startswith('-e'):
      replace_i = i
      break
  if replace_i:
    l[i] = '-e .'
  else:
    raise Exception("Line with -e not found in requirements.txt!")

  with open('requirements.txt', 'w') as outf:
    outf.write('\n'.join(filter(None, sorted(l))))
  logger.info('Updated requirements.txt via pip freeze.')


@manager.command
def migrate():
  """Outputs the command to migrate this database.
  """
  print """
Run `flask db init`

Run `flask db migrate`
	"""


@manager.command
def test(coverage=False, test_name=None):
  """Run the unit tests."""
  import unittest
  if test_name is None:
    tests = unittest.TestLoader().discover('testing')
  else:
    tests = unittest.TestLoader().loadTestsFromName('testing.' + test_name)
  unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == "__main__":
  if not os.path.exists('./requirements.txt'):
    raise Exception("You must run manage.py in the root directory of hedgehog")
  manager.run()
