import os
from datetime import timedelta

# Determine the folder of the top-level directory of this project
BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    FLASK_ENV = os.getenv('FLASK_ENV', default='development')
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='BAD_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL',
                                        default=f"sqlite:///{os.path.join(BASEDIR, 'instance', 'app.db')}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 15
    WTF_CSRF_ENABLED = True
    REMEMBER_COOKIE_DURATION = timedelta(days=14)

    # Flask-Mail Configuration
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    #MAIL_USE_SSL = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', default='')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', default='')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_USERNAME', default='')

    # CSRF protection is enabled by default in Flask-WTF, I like to explicitly set

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
    BCRYPT_LOG_ROUNDS = 4
