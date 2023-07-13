from flask_app import app
from flask import render_template , redirect, request

from flask_app.models.model_dealer import Dealer
from flask_app.models.model_car import Car

#landing page
@app.route('/')
def landing():
    #to get the dealers
    #contact the class
    #select the get_all method
    #store into a variable
    all_cars = Car.get_all()
    all_dealers = Dealer.get_all()
    return render_template("index.html", all_dealers= all_dealers, all_cars = all_cars)