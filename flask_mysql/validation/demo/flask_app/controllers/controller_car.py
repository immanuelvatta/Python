from flask_app import app
from flask import render_template , redirect, request

from flask_app.models.model_dealer import Dealer
from flask_app.models.model_car import Car




@app.route('/car/new')
def car_new():
    all_dealers = Dealer.get_all()
    all_cars = Car.get_all()
    return render_template("car_new.html", all_dealers = all_dealers)

@app.route('/car/create', methods=['POST'])
def car_create():
    
    #target the class
    #select the method
    #have a return
    data = {
        **request.form
    }
    id = Car.create(data)
    return redirect('/')