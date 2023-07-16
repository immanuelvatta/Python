from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

#READ
@app.route('/users')
def display_users():
    # calling to 
    all_users = User.get_all()
    # passing all users to our template so we can display them there
    return render_template("display_users.html", users = all_users)

#CREATE
@app.route('/users/create', methods=['POST'])
def create():
    User.create(request.form)
    return redirect('/users')

@app.route('/users/new')
def create_users():
    return render_template('create_users.html')

@app.route('/users/show/<int:id>')
def display_user(id):
    data = {
        'id' : id
    }
    user = User.get_one(data)
    return render_template('display_user.html', user = user)

#update
@app.route('/users/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')


@app.route('/users/edit/<int:id>')
def update_user(id):
    data = {
        'id' : id
    }
    user= User.get_one(data)
    return render_template('update_user.html', user = user)

#delete
@app.route('/users/delete/<int:id>')
def delete(id):
    data = {
        'id' : id
    }
    User.delete(data)
    return redirect('/users')

if __name__=="__main__":
    app.run(debug=True)
