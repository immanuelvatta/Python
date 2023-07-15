from flask_app import app

from flask import render_template, redirect, request


from flask_app.models.model_dojo import Dojo
from flask_app.models.model_ninja import Ninja

#* '/dojo/new' -> display the route with the form 
@app.route('/dojo/new')
def dojo_new():
    return render_template('dojo_new.html')

#* '/dojo/create' -> process the form from above
@app.route('/dojo/create', methods=['POST'])
def dojo_create():
    #do the creating
    data = {
        **request.form 
    }
    Dojo.create(data)
    return redirect('/')

#* '/dojo/<int:id>' -> display the dojo's info -> Show
@app.route('/dojo/<int:id>')
def dojo_show(id):
    
    the_dojo = Dojo.get_one({'id':id})
    return render_template("dojo_show.html", the_dojo= the_dojo)

#* '/dojo/<int:id>/edit' -> display the dojo's info in a form so that they can edit it
@app.route('/dojo/<int:id>/edit')
def dojo_edit(id):
    return render_template("dojo_edit.html")

#* '/dojo/<int:id>/update' -> process the edit form
@app.route('/dojo/<int:id>/update', methods=['POST'])
def dojo_update(id):
    return redirect('/')

#* '/dojo/<int:id>/delete' -> delete the dojo at that id
@app.route('/dojo/<int:id>/delete')
def dojo_delete(id):
    return redirect('/')

# '/dojo/new' -> display the route with the form
# '/dojo/create' -> process the form from above
# '/dojo/<int:id>' -> display the dojo's info -> Show
# '/dojo/<int:id>/edit' -> display the dojo's info in a form so that they can edit it
# '/dojo/<int:id>/update' -> process the edit form
# '/dojo/<int:id>/delete' -> delete the dojo at that id