import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'fmi',
    version = '0.0.1',
    author = 'Gerald Kaszuba',
    author_email = 'fmi@gakman.com',
    description = ('A simple Python interface to Find My iPhone on the '
        'Mobile Me service'),
    license = 'BSD',
    keywords = 'iphone findmyiphone me.com mobileme',
    url = 'http://slowchop.com/',
    packages=['fmi'],
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: BSD License',
    ],
)

