from setuptools import setup
import sys

if sys.version_info < (3, 0):
    sys.exit('Sorry, Python < 3 is not supported')

setup(name='downloads',
      version='0.0.1',
      description='Easy HTTP downloads',
      url='https://github.com/audy/downloads',
      author='Austin Davis-Richardson',
      author_email='harekrishna@gmail.com',
      packages=['downloads'])
