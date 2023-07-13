from flask_app import app
from flask import render_template, redirect

from flask_app.models.model_user import User


@app.route('/')
def index():
    
    # user= User.get_one({'id': 3})
    return render_template('index.html')


@app.errorhandler(404)
def page_404(e):
    return render_template("page_404.html")