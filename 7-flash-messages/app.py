from flask import Flask, escape, render_template, request, session, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = '\x8ac\x93\xbe1\xd4\xa6\xf7\xc3\x0e\x88\xf8\x1b\xfa\xad\xa3l\xa0\x07\xa5l\xd2X\x99\xa3\x9aH\xbcyT\xf5#'



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

        # url_for() function is used to generate a URL based on a specific view function 
        return redirect(url_for('list_stocks')) 

    return render_template('add_stock.html')

@app.route('/stocks/')
def list_stocks():
    return render_template('stocks.html')