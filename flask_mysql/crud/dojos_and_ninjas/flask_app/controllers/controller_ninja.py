from flask_app import app

from flask import render_template, redirect, request


from flask_app.models.model_ninja import Ninja
from flask_app.models.model_dojo import Dojo

#* '/ninja/new' -> display the route with the form 
@app.route('/ninja/new')
def ninja_new():
    all_dojos = Dojo.get_all()
    return render_template('ninja_new.html', all_dojos=all_dojos)

#* '/ninja/create' -> process the form from above
@app.route('/ninja/create', methods=['POST'])
def ninja_create():
    #do the creating
    data = {** request.form}
    Ninja.create(data)
    return redirect('/')

#* '/ninja/<int:id>' -> display the ninja's info -> Show
@app.route('/ninja/<int:id>')
def ninja_show(id):
    
    return render_template("ninja_show".html)

#* '/ninja/<int:id>/edit' -> display the ninja's info in a form so that they can edit it
@app.route('/ninja/<int:id>/edit')
def ninja_edit(id):
    return render_template("ninja_edit.html")

#* '/ninja/<int:id>/update' -> process the edit form
@app.route('/ninja/<int:id>/update', methods=['POST'])
def ninja_update(id):
    return redirect('/')

#* '/ninja/<int:id>/delete' -> delete the ninja at that id
@app.route('/ninja/<int:id>/delete')
def ninja_delete(id):
    return redirect('/')

# '/ninja/new' -> display the route with the form
# '/ninja/create' -> process the form from above
# '/ninja/<int:id>' -> display the ninja's info -> Show
# '/ninja/<int:id>/edit' -> display the ninja's info in a form so that they can edit it
# '/ninja/<int:id>/update' -> process the edit form
# '/ninja/<int:id>/delete' -> delete the ninja at that id