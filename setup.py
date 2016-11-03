import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid==1.6',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'pyramid_fanstatic',
    'pyramid_jinja2',
    'MySQL-python',
    'PyCrypto',
    'WebHelpers',
    'Babel',
    'lingua',
    'xlsxwriter',
    ]

setup(name='Climmob3',
      version='0.0',
      description='Climmob3',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='climmob3',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = climmob3:main
      [fanstatic.libraries]
      climmob3 = climmob3.resources:library
      [console_scripts]
      initialize_Climmob3_db = climmob3.scripts.initializedb:main
      """,
      )
