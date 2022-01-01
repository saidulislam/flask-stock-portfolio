from flask import Flask
from logging.handlers import RotatingFileHandler
import logging
from flask.logging import default_handler
import os


######################################
#### Application Factory Function ####
######################################

def create_app():
    # Create the Flask application
    app = Flask(__name__)

    # Configure the Flask application
    config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(config_type)

    register_blueprints(app)
    configure_logging(app)

    return app


def register_blueprints(app):
    # Import the blueprints
    from project.stocks import stocks_blueprint
    from project.users import users_blueprint

    # Since the application instance is now created, register each Blueprint
    # with the Flask application instance (app)
    app.register_blueprint(stocks_blueprint)
    app.register_blueprint(users_blueprint, url_prefix='/users')


def configure_logging(app):
    # Logging Configuration
    # once the log file gets close to the specified file size (maxBytes=16384), 
    # it will move that log file to flask-stock-portfolio.log.1 and continue 
    # logging with a new flask-stock-portfolio.log file. The backupCount=20 
    # argument specifies that up to 20 log files can be saved before the log 
    # files are overwritten.
    file_handler = RotatingFileHandler('instance/flask-stock-portfolio.log',
                                       maxBytes=16384,
                                       backupCount=20)
    file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(filename)s:%(lineno)d]')
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    # Remove the default logger configured by Flask
    app.logger.removeHandler(default_handler)

    app.logger.info('Starting the Flask Stock Portfolio App...')

