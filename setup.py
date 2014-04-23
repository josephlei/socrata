from distutils.core import setup

from socrata import __version__

setup(name='socrata',
      author='Thomas Levine',
      author_email='_@thomaslevine.com',
      description='Download data from Socrata open data portals.',
      url='https://github.com/tlevine/socrata',
      packages=['socrata'],
      install_requires = ['pickle_warehouse','requests'],
      extras_require = [],
      tests_require = ['nose'],
      version=__version__,
      license='AGPL',
)
