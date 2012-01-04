"""
Flask-Tweepy
------------

Tweet easily from Flask applications.
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

