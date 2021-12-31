from flask import Flask, escape, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    # To pass in data to include when the template is rendered
    return render_template('about.html', company_name="saidulislam.com")
    # return render_template('about.html')

@app.route('/add_stock', methods=['GET', 'POST'])
def add_stock():
    if request.method == 'POST':
        for key, value in request.form.items():
            # print the form data to the console
            print(f'{key}: {value}')
            
    return render_template('add_stock.html')
