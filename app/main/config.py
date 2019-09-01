import os

_postgres_local_base = os.getenv('DATABASE_URL', 'postgresql://jnwanya:k0l0@localhost/forum')
_app_secret_key = os.getenv('SECRET_KEY', 'p@ssw0rd')
_base_dir = os.path.abspath(os.path.dirname(__file__))

ACCESS_TOKEN_EXPIRY_TIME_MINUTES = 60
REFRESH_TOKEN_EXPIRY_TIME_MINUTES = 60 * 24


class Config:
    JWT_SECRET_KEY = _app_secret_key
    JWT_ACCESS_TOKEN_EXPIRES = ACCESS_TOKEN_EXPIRY_TIME_MINUTES * 60
    JWT_REFRESH_TOKEN_EXPIRES = REFRESH_TOKEN_EXPIRY_TIME_MINUTES * 60
    DEBUG = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = _postgres_local_base
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_base_dir, 'forum_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = _postgres_local_base


config_by_name = dict(dev=DevelopmentConfig, test=TestingConfig, prod=ProductionConfig)
key = Config.JWT_SECRET_KEY
