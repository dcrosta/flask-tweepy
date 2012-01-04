import unittest

import flask
from flask.ext.tweepy import Tweepy

class FlaskTweepyConfigTest(unittest.TestCase):

    def setUp(self):
        self.app = flask.Flask('test')
        self.context = self.app.test_request_context('/')
        self.context.push()

    def tearDown(self):
        self.context.pop()

    def test_default_config_prefix(self):
        self.app.config['TWEEPY_CONSUMER_KEY'] = 'keykeykey'
        self.app.config['TWEEPY_CONSUMER_SECRET'] = 'secretsecret'
        self.app.config['TWEEPY_ACCESS_TOKEN_KEY'] = 'keykeykey'
        self.app.config['TWEEPY_ACCESS_TOKEN_SECRET'] = 'secretsecret'

        tweepy = Tweepy(self.app)
        assert tweepy.api is not None

    def test_custom_config_prefix(self):
        self.app.config['CUSTOM_CONSUMER_KEY'] = 'keykeykey'
        self.app.config['CUSTOM_CONSUMER_SECRET'] = 'secretsecret'
        self.app.config['CUSTOM_ACCESS_TOKEN_KEY'] = 'keykeykey'
        self.app.config['CUSTOM_ACCESS_TOKEN_SECRET'] = 'secretsecret'

        tweepy = Tweepy(self.app, config_prefix='CUSTOM')
        assert tweepy.api is not None

    def test_multiple_tweepys(self):
        self.app.config['TWEEPY_CONSUMER_KEY'] = 'keykeykey'
        self.app.config['TWEEPY_CONSUMER_SECRET'] = 'secretsecret'
        self.app.config['TWEEPY_ACCESS_TOKEN_KEY'] = 'keykeykey'
        self.app.config['TWEEPY_ACCESS_TOKEN_SECRET'] = 'secretsecret'

        tweepy1 = Tweepy(self.app)
        assert tweepy1.api is not None

        self.app.config['CUSTOM_CONSUMER_KEY'] = 'keykeykey'
        self.app.config['CUSTOM_CONSUMER_SECRET'] = 'secretsecret'
        self.app.config['CUSTOM_ACCESS_TOKEN_KEY'] = 'keykeykey'
        self.app.config['CUSTOM_ACCESS_TOKEN_SECRET'] = 'secretsecret'

        tweepy2 = Tweepy(self.app, config_prefix='CUSTOM')
        assert tweepy2.api is not None

        assert tweepy1.api is not tweepy2.api

    def test_fails_without_required_configs(self):
        self.app.config['TWEEPY_CONSUMER_KEY'] = 'keykeykey'
        # self.app.config['TWEEPY_CONSUMER_SECRET'] = 'secretsecret'
        self.app.config['TWEEPY_ACCESS_TOKEN_KEY'] = 'keykeykey'
        self.app.config['TWEEPY_ACCESS_TOKEN_SECRET'] = 'secretsecret'

        self.assertRaises(Exception, Tweepy, self.app)

    def test_api_is_none_if_unconfigured(self):
        tweepy = Tweepy()

        assert tweepy.api is None

    def test_init_app(self):
        tweepy = Tweepy()

        self.app.config['TWEEPY_CONSUMER_KEY'] = 'keykeykey'
        self.app.config['TWEEPY_CONSUMER_SECRET'] = 'secretsecret'
        self.app.config['TWEEPY_ACCESS_TOKEN_KEY'] = 'keykeykey'
        self.app.config['TWEEPY_ACCESS_TOKEN_SECRET'] = 'secretsecret'

        tweepy.init_app(self.app)
        assert tweepy.api is not None

    def test_fails_with_duplicate_config_prefix(self):
        self.app.config['TWEEPY_CONSUMER_KEY'] = 'keykeykey'
        self.app.config['TWEEPY_CONSUMER_SECRET'] = 'secretsecret'
        self.app.config['TWEEPY_ACCESS_TOKEN_KEY'] = 'keykeykey'
        self.app.config['TWEEPY_ACCESS_TOKEN_SECRET'] = 'secretsecret'

        Tweepy(self.app)
        self.assertRaises(Exception, Tweepy, self.app)

