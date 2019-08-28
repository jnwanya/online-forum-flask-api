import os

_postgres_local_base = os.getenv('DATABASE_URL', 'postgresql://jnwanya:k0l0@localhost/forum')
_app_secret_key = os.getenv('SECRET_KEY', 'p@ssw0rd')
_base_dir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = _app_secret_key
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
key = Config.SECRET_KEY
