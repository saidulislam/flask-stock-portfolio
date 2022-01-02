"""
The stocks blueprint handles the user management for this application.
Specifically, this blueprint allows for users to add, edit, and delete
stock data from their portfolio.
"""
from flask import Blueprint

# specifies the name of the blueprint ('stocks') and it specifies the location 
# of the template files within the blueprint. Additionally, the last line imports 
# the routes that we'll create in routes.py.
stocks_blueprint = Blueprint('stocks', __name__, template_folder='templates')

from . import routes
