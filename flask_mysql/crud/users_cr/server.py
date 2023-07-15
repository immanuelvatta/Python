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
    return render_template("read.html", users=all_users)

#CREATE
@app.route('/users/create', methods=['POST'])
def create():
    User.save(request.form)
    return redirect('/users')

@app.route('/users/new')
def new():
    return render_template('create.html')


if __name__=="__main__":
    app.run(debug=True)
