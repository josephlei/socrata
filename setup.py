from distutils.core import setup

from pickle_warehouse import __version__

setup(name='pickle-warehouse',
      author='Thomas Levine',
      author_email='_@thomaslevine.com',
      description='Download data from Socrata open data portals.',
      url='https://github.com/tlevine/socrata',
      packages=['socrata'],
      install_requires = ['pickle_warehouse'],
      extras_require = [],
      tests_require = ['nose'],
      version=__version__,
      license='AGPL',
)
