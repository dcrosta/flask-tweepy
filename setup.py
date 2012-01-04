"""
Flask-Tweepy
------------

Tweet easily from Flask applications.

Installation
============

Flask-Tweepy is pip-installable:

    pip install Flask-Tweepy

You can install the latest development snapshot like so:

    pip install http://github.com/dcrosta/flask-tweepy/tarball/master#egg=Flask-Tweepy-dev

Development
===========

Source code is hosted in `GitHub <https://github.com/dcrosta/flask-tweepy>`_
(contributions are welcome!)
"""

from setuptools import setup

setup(
    name='Flask-Tweepy',
    version='0.1',
    url='http://flask-tweepy.readthedocs.org/',
    license='BSD',
    author='Dan Crosta',
    author_email='dcrosta@late.am',
    description='Tweet easily from Flask applications',
    long_description=__doc__,
    zip_safe=False,
    platforms='any',
    py_modules=['flask_tweepy'],
    install_requires=[
        'Flask >= 0.8',
        'tweepy >= 1.8, <1.9',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    tests_require=[
        'nose',
    ],
    test_suite='nose.collector',
)

