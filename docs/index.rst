Flask-Tweepy
============

Flask-Tweepy brings `Tweepy <http://packages.python.org/tweepy/html/>`_
support to Flask applications, with simple configuration and easy access to
Tweepy's :class:`~tweepy.API` class.

Installation
------------

Installation is a breeze with `pip <http://www.pip-installer.org/>`_:

.. code-block:: console

    $ pip install Flask-Tweepy

Source code is avilable `on GitHub
<https://github.com/dcrosta/flask-tweepy>`_.

Quickstart
----------

Flask-Tweepy uses OAuth to authenticate to Twitter's API servers. You'll
need your application's Consumer Key and Consumer Secret, which you can
create or obtain at `the Twitter Developers website
<https://dev.twitter.com/apps>`_.

Flask-Tweepy 0.1 currently only supports connecting as the user who
registered the application (that is, you can only update the status of that
user). To update statuses, you will also need the Access Token Key and
Access Token Secret, which you can create or retrieve on the Twitter
Developers website.

.. note::

   In a future release, Flask-Tweepy will support OAuth authentication for
   end-users, which will allow your application to tweet as your end users,
   retrieve their timeline, etc. In this mode, it will not be necessary to
   obtain or configure the Access Token Key and Secret.


.. code-block:: python

    from flask import Flask
    from flask.ext.tweepy import Tweepy

    app = Flask(__name__)
    app.config.setdefault('TWEEPY_CONSUMER_KEY', 'consumer-key-here')
    app.config.setdefault('TWEEPY_CONSUMER_SECRET', 'consumer-secret-here')
    app.config.setdefault('TWEEPY_ACCESS_TOKEN_KEY', 'access-token-key-here')
    app.config.setdefault('TWEEPY_ACCESS_TOKEN_SECRET', 'access-token-secret-here')

    tweepy = Tweepy(app)


The ``tweepy`` object then gives you access to the Tweepy API with the
:attr:`~flask_tweepy.Tweepy.api` property:

.. code-block:: python

    @app.route('/tweets')
    def show_tweets():
        tweets = tweepy.api.public_timeline()
        return render_template('tweets.html', tweets=tweets)

    @app.route('/say-something')
    def say_something():
        status = tweepy.api.update_status('Hello, world!')
        status_link = 'http://twitter.com/#!/YourUserName/status/%s' % status.id
        return render_template('what_i_said.html', status_link=status_link)

.. note::

   In order to update statuses from Flask-Tweepy, your application will need
   the Read and Write access level. You can configure this in the Twitter
   Developers page for your application (by default, new Twitter
   applications are read-only). If you generated an Access Token while your
   application was read-only, you will need to regenerate the Token once you
   have reconfigured the access level.


Configuration
-------------

======================= ====================================================
``CONSUMER_KEY``        The Consumer Key, which you can acquire from the
                        Twitter Developers site page for your application.
``CONSUMER_SECRET``     The Consumer Secret.
``ACCESS_TOKEN_KEY``    The Access Token Key (also known as the "Access
                        Token" on Twitter's site) for your user for your
                        application.
``ACCESS_TOKEN_SECRET`` The Access Token Secret for your user for your
                        application.
======================= ====================================================

These configuration variable names are appended to the "config prefix,"
which is "TWEEPY" by default. You can change the config prefix with the
`config_prefix` argument to :class:`~flask_tweepy.Tweepy`.

This technique can be used to create multiple :class:`~flask_tweepy.Tweepy`
instances in your application:

.. code-block:: python

    from flask import Flask
    from flask.ext.tweepy import Tweepy

    app = Flask(__name__)

    app.config.setdefault('TWEEPY_CONSUMER_KEY', 'consumer-key-here')
    app.config.setdefault('TWEEPY_CONSUMER_SECRET', 'consumer-secret-here')
    app.config.setdefault('TWEEPY_ACCESS_TOKEN_KEY', 'access-token-key-here')
    app.config.setdefault('TWEEPY_ACCESS_TOKEN_SECRET', 'access-token-secret-here')
    tweepy1 = Tweepy(app)

    app.config.setdefault('CUSTOM_CONSUMER_KEY', 'consumer-key-here')
    app.config.setdefault('CUSTOM_CONSUMER_SECRET', 'consumer-secret-here')
    app.config.setdefault('CUSTOM_ACCESS_TOKEN_KEY', 'access-token-key-here')
    app.config.setdefault('CUSTOM_ACCESS_TOKEN_SECRET', 'access-token-secret-here')
    tweepy1 = Tweepy(app, config_prefix='CUSTOM')

API
---

.. autoclass:: flask_tweepy.Tweepy
   :members:

