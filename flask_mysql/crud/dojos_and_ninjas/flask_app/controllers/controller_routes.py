from flask_app import app

from flask import render_template, redirect, request

from flask_app.models.model_dojo import Dojo
from flask_app.models.model_ninja import Ninja

#landing page
@app.route('/')
def landing():
    
    all_dojos = Dojo.get_all()
    return render_template("dojos.html", all_dojos = all_dojos)