from flask import Flask, escape, render_template, request, session, redirect, url_for, flash
from flask.logging import default_handler
from logging.handlers import RotatingFileHandler
import logging


app = Flask(__name__)
app.secret_key = '\x8ac\x93\xbe1\xd4\xa6\xf7\xc3\x0e\x88\xf8\x1b\xfa\xad\xa3l\xa0\x07\xa5l\xd2X\x99\xa3\x9aH\xbcyT\xf5#'

# Remove the default logger configured by Flask
app.logger.removeHandler(default_handler)

# Logging Configuration
# once the log file gets close to the specified file size (maxBytes=16384), 
# it will move that log file to flask-stock-portfolio.log.1 and continue 
# logging with a new flask-stock-portfolio.log file. The backupCount=20 
# argument specifies that up to 20 log files can be saved before the log 
# files are overwritten.
file_handler = RotatingFileHandler('flask-stock-portfolio.log',
                                   maxBytes=16384,
                                   backupCount=20)
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(filename)s:%(lineno)d]')
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.INFO) # minimum log level you want
app.logger.addHandler(file_handler)

# Log that the Flask application is starting
app.logger.info('Starting the Flask Stock Portfolio App...')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    flash('Thanks for learning about this site!', 'info')
    
    # To pass in data to include when the template is rendered
    return render_template('about.html', company_name="saidulislam.com")
    # return render_template('about.html')

@app.route('/add_stock', methods=['GET', 'POST'])
def add_stock():
    if request.method == 'POST':
        # DEBUG - Print the form data to the console
        for key, value in request.form.items():
            print(f'{key}: {value}')

        # Save the form data to the session object
        session['stock_symbol'] = request.form['stock_symbol']
        session['number_of_shares'] = request.form['number_of_shares']
        session['purchase_price'] = request.form['purchase_price']

        flash(f"Added new stock ({ request.form['stock_symbol'] })!", 'success')

        app.logger.info(f"Added new stock ({ request.form['stock_symbol'] })!")

        # url_for() function is used to generate a URL based on a specific view function 
        return redirect(url_for('list_stocks')) 

    return render_template('add_stock.html')

@app.route('/stocks/')
def list_stocks():
    return render_template('stocks.html')