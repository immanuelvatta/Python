from flask_app import app
from flask import render_template , redirect, request

from flask_app.models.model_dealer import Dealer
#landing page
@app.route('/')
def landing():
    #to get the dealers
    #contact the class
    #select the get_all method
    #store into a variable
    
    all_dealers = Dealer.get_all()
    return render_template("index.html", all_dealers= all_dealers)


#             table action
@app.route('/dealer/new')
def dealer_new():
    return render_template("dealer_new.html")

@app.route("/dealer/create", methods=['POST'])
def dealer_create():
    #get data from form
    data = {
        **request.form
    }
    #pass data to model
    dealer_id = Dealer.create(data)
    return redirect('/')

#
@app.route('/dealer/<int:dealer_id>/delete')
def dealer_delete(dealer_id):
    #contact the class
    data = {
        #i misspelled id in db so its it now
        'id' : dealer_id
    }
    Dealer.delete_one(data)
    return redirect('/')
    #select the method
    #return a redirect