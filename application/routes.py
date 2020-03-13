from flask import render_template
from application import app

@app.route('/home')
def home():
    render_template('home.html', title='Home')