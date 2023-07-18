from flask_app import app
from flask import render_template , redirect, request, session, flash

from flask_app.models.model_dealer import Dealer
from flask_app.models.model_car import Car

#landing page
@app.route('/')
def landing():
    # think of session like a dictionary 
    #if we want a key from session
    #session['key']
    dealer = None # can replace None with "" or False, or None
    if 'dealer_id' in session:
        dealer = Dealer.get_one({'id': session['dealer_id']})
    #to get the dealers
    #contact the class
    #select the get_all method
    #store into a variable
    all_cars = Car.get_all()
    all_dealers = Dealer.get_all()
    return render_template("index.html", all_dealers= all_dealers, all_cars = all_cars, dealer = dealer)


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login/process', methods = ['POST'])
def login_process():
    
    
    is_valid = Dealer.validator_login(request.form)
    if is_valid == False:
        return redirect('/login')
        
    # potential_dealer = Dealer.get_one_by_username({'username': given_email})
    # given_email = request.form['email']
    # given_password = request.form['password']
    # if not potential_dealer:
    #     return redirect('/login')
    # if potential_dealer.password == given_password:
    #     print("YEAH!")
    #     session['dealer_id'] = potential_dealer.id
    # else:
    #     print("BOO")
    #     return redirect('/login')
    return redirect('/')

@app.route('/logout')
def logout():
    del session['dealer_id']
    return redirect('/')