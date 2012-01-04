from flask import current_app
import tweepy

class Tweepy(object):
    """The :class:`~flask_tweepy.Tweepy` class configures and creates a
    :class:`tweepy.API` instance based on Flask configuration variables.
    Instantiating a :class:`~flask_tweepy.Tweepy` with no arguments does not
    configure the :class:`tweepy.API`, and will not be usable unless
    :meth:`Tweepy.init_app` is subsequently called.

    :param flask.Flask app: the Flask application to which this Tweepy
       should be attached
    :param str config_prefix: the configuration variable prefix
    """

    def __init__(self, app=None, config_prefix='TWEEPY'):
        # this is overridden by init_app if app is supplied
        self.config_prefix = None
        if app is not None:
            self.init_app(app, config_prefix)

    def init_app(self, app, config_prefix='TWEEPY'):
        """Initialize this :class:`~flask_tweepy.Tweepy` if no arguments were
        given to the constructor. Accepts the same arguments as the
        constructor.
        """
        app.extensions.setdefault('tweepy', {})

        if config_prefix in app.extensions['tweepy']:
            raise Exception('duplicate config_prefix "%s"' % config_prefix)

        self.config_prefix = config_prefix

        consumer_key = app.config.get('%s_CONSUMER_KEY' % config_prefix)
        consumer_secret = app.config.get('%s_CONSUMER_SECRET' % config_prefix)
        token_key = app.config.get('%s_ACCESS_TOKEN_KEY' % config_prefix)
        token_secret = app.config.get('%s_ACCESS_TOKEN_SECRET' % config_prefix)

        if not all((consumer_key, consumer_secret)):
            raise Exception('%s_CONSUMER_KEY and %s_CONSUMER_SECRET '
                            'are required' % (config_prefix, config_prefix))

        # TODO 0.2: allow tweets as users of the app,
        # so don't require token_key and token_secret
        if not all((token_key, token_secret)):
            raise Exception('%s_ACCESS_TOKEN_KEY and %s_ACCESS_TOKEN_SECRET '
                            'are required' % (config_prefix, config_prefix))

        # TODO 0.2: support callback_url
        auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
        if all((token_key, token_secret)):
            auth.set_access_token(token_key, token_secret)

        api = tweepy.API(auth)
        app.extensions['tweepy'][config_prefix] = (auth, api)

    @property
    def api(self):
        """Return the :class:`tweepy.API` object if Flask-Tweepy has been
        properly configured and initialized, else return None.
        """
        tweepies = current_app.extensions.get('tweepy', {})
        auth, api = tweepies.get(self.config_prefix, (None, None))
        return api

