import os


class Config(object):
    FLASK_ENV = os.getenv('FLASK_ENV', default='development')
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='BAD_SECRET_KEY')
    # BAD_SECRET_KEY is a (really) bad value for the secret key. 
    # It's fine to leave this as the default, but make sure the 
    # production environment variable is randomly generated so 
    # it's difficult to guess.
    # example of how you can generate one
    # (venv) $ python
    # >>> import secrets
    # >>> print(secrets.token_bytes(32))

    # According to the documentation here 
    # (https://flask.palletsprojects.com/en/1.1.x/config/#environment-and-debug-features) 
    # you shouldn't set Debug and ENV via code, otherwise, some extension can misunderstand 
    # that and act unexpectedly.
    #
    # Per official doc
    # While it is possible to set ENV and DEBUG in your config or code, 
    # this is strongly discouraged. They can’t be read early by the flask command, 
    # and some systems or extensions may have already configured themselves based 
    # on a previous value.


class ProductionConfig(Config):
    FLASK_ENV = 'production'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
