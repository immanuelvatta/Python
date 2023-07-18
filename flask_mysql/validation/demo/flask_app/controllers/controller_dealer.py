from flask_app import app, bcrypt
from flask import render_template , redirect, request

from flask_app.models.model_dealer import Dealer



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
    is_valid = Dealer.validator(data)
    if is_valid== False:
        return redirect('/dealer/new')
    
    # do the hashing....
    #generate a new hash
    hash_pw = bcrypt.generate_password_hash(data['password'])
    #update the data dictionary for password
    data['password'] = hash_pw
    
    #pass data to model
    dealer_id = Dealer.create(data)
    return redirect('/')

@app.route('/dealer/<int:id>')
def dealer_show(id):
    the_dealer = Dealer.get_one({'id':id})
    print(the_dealer)
    #get the dealer's info
    return render_template('dealer_show.html', the_dealer = the_dealer)

@app.route('/dealer/<int:dealer_id>/delete')
def dealer_delete(dealer_id):
    #contact the class
    data = {
        #id was  misspelled id in db so was it now
        'id' : dealer_id
    }
    Dealer.delete_one(data)
    return redirect('/')
    #select the method
    #return a redirect