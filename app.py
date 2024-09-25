# IMPORTS
from flask import Flask, render_template

# FLASK INIT
app = Flask(__name__)

# FUNCTIONS


# FLASK ROUTES
@app.route('/')
@app.route('/index')
def index():
    title = 'Random group generator'
    return render_template('index.html', title=title)