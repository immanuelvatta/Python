from flask_app import app

from flask import render_template, redirect


#fills out the form 
@app.route('/user/new')
def user_new():
    return render_template('user_new.html')

#process  the form
@app.route('/user/create', methods=['POST'])
def user_create():
    #do the creating
    return redirect('/')


@app.route('/user/<int:id>')
def user_show(id):
    return render_template("user_show".html)

@app.route('/user/<int:id>/edit')
def user_edit(id):
    return render_template("user_edit.html")

@app.route('/user/<int:id>/update', methods=['POST'])
def user_update(id):
    return redirect('/')

@app.route('/user/<int:id>/delete')
def user_delete(id):
    return redirect('/')

# '/user/new' -> display the route with the form
# '/user/create' -> process the form from above
# '/user/<int:id>' -> display the user's info -> Show
# '/user/<int:id>/edit' -> display the user's info in a form so that they can edit it
# '/user/<int:id>/update' -> process the edit form
# '/user/<int:id>/delete' -> delete the user at that id