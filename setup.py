#MonkeyBall/setup.py
import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES')).read()

entry_points = """
    [paste.app_factory]
    main = monkeyball:main
"""

requires = [
    'pyramid==1.3',
    'pyramid_debugtoolbar',
    'sqlalchemy',
    'psycopg2',
    'alembic',
    'waitress',
    'velruse',
    'retools',
    'APScheduler',
    'redis'
]

tests_require = requires + [
    'nose',
]

setup(name='monkeyball',
      version='0.1dev',
      description='',
      long_description=README + '\n\n' + CHANGES,
      install_requires=requires,
      tests_require=tests_require,
      url='http://localhost',
      packages=['monkeyball'],
      test_suite='monkeyball.tests',
      entry_points=entry_points
)
