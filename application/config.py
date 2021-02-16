import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Base Config"""


class ProductionConfig(Config):
    """Production Config"""


class DevelopmentConfig(Config):
    """Dev Config"""


class TestingConfig(Config):
    """Testing Config"""

    TESTING = True
