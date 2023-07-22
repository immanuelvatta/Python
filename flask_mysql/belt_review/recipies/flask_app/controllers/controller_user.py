from flask_app import app, bcrypt

from flask import render_template, redirect, request, session

#TODO change this
from flask_app.models.model_user import User
from flask_app.models.model_recipes import Recipe

@app.route('/user/new')
def user_new():
    return redirect('/user/success')


@app.route('/user/create', methods=['POST'])
def user_create():
    
    
    data = {
        **request.form
    }
    if not User.validator(data):
        return redirect('/')
    
    
    hash_pw = bcrypt.generate_password_hash(data['password'])
    print(data['password'])
    data['password'] = hash_pw
    print(data['password'])
    #do the creating
    User.create(data)
    # session['user_id'] = user_id
    session['email'] = request.form['email']
    
    
    #use session 
    return redirect('/user/success')

@app.route('/user/login', methods=['POST'])
def user_login():
    is_valid = User.validator_login(request.form)
    if is_valid == False:
        return redirect('/')
    else:
        session['email'] = is_valid
    
    return redirect('/user/success')

@app.route('/user/success')
def success():
    if not session:
        return redirect('/')
    user = User.get_one(session['email'])

    recipes = Recipe.get_all()
    return render_template("success.html", user= user, recipes = recipes)


@app.route('/user/logout')
def logout():
    session.clear()
    return redirect('/')

# '/user/new' -> display the route with the form
# '/user/create' -> process the form from above
# '/user/<int:id>' -> display the user's info -> Show
# '/user/<int:id>/edit' -> display the user's info in a form so that they can edit it
# '/user/<int:id>/update' -> process the edit form
# '/user/<int:id>/delete' -> delete the user at that id
