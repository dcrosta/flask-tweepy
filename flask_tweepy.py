from flask import current_app
import tweepy

class Tweepy(object):

    def __init__(self, app=None, config_prefix='TWEEPY'):
        if app is not None:
            self.init_app(app, config_prefix)

    def init_app(self, app, config_prefix='TWEEPY'):
        if 'tweepy' not in app.extensions:
            app.extensions['tweepy'] = {}

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
        if 'tweepy' not in current_app.extensions:
            raise Exception('current app does not have tweepy extensions')
        if self.config_prefix not in current_app.extensions['tweepy']:
            raise Exception('unknown/misconfigured tweepy: "%s" not in '
                            'current_app.extensions' % self.config_prefix)
        auth, api = current_app.extensions['tweepy'][self.config_prefix]
        return api

