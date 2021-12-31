from flask import Flask, escape

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"

@app.route("/about")
def about():
    return '<h2>About this application...</h2>'

@app.route("/example", methods=['GET', 'POST'])
def example():
    return 'an example'

@app.route('/stocks/')
def stocks():
    return '<h2>Stock List...</h2>'

# variable routing
@app.route('/hello/<message>')
def hello_message(message):
    # escape() function is to prevent a Cross-Site Scripting (XSS) attack 
    return f'<h1>Welcome {escape(message)}!</h1>'

# variable route types
# Accepted variable types - string, int, path, uuid
@app.route('/blog_posts/<int:post_id>')
def display_blog_post(post_id):
    return f'<h1>Blog Post #{post_id}...</h1>'
