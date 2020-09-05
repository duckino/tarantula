from setuptools import setup

setup(
   name='tarantula',

   version='0.0.1',

   author='duckino',
   url = 'https://github.com/duckino/taratula',
   license = 'MIT',
   packages=['tarantula'],

   description = 'Web Scrapper with Automation and Learning',
   long_description=open('README.md').read(),
   install_requires=[
       "pytest",
       "pytube3",
       "typing-extensions",
       "requests",
       "bs4"
   ],
)