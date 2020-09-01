from setuptools import setup

setup(
   name='tarantula',
   version='0.0.1',
   author='duckino',
  #  author_email='aac@example.com',
   packages=['tarantula'],
  #  scripts=['bin/script1','bin/script2'],
  #  url='http://pypi.python.org/pypi/PackageName/',
  #  license='LICENSE.txt',
  #  description='An awesome package that does something',
   long_description=open('README.md').read(),
   install_requires=[
       "pytest",
       "pytube3 == 9.6.4",
       "typing-extensions == 3.7.4.2"
   ],
)