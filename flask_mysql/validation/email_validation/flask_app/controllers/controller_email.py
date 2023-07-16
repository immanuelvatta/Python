from flask_app import app

from flask import render_template, redirect, request
from flask_app.models.model_email import Email
#TODO change this

#fills out the form 
@app.route('/')
def index():
    return render_template('index.html')

#process  the form
@app.route('/email/create', methods=['POST'])
def email_create():
    if not Email.is_valid_email(request.form):
        return redirect('/')
    #do the creating
    Email.create(request.form)
    return redirect('/email/display')


@app.route('/email/display')
def email_display():
    emails = Email.get_all()
    return render_template("display_emails.html", emails = emails)



@app.route('/email/delete/<int:id>')
def email_delete(id):
    data = {
        'id' : id
    }
    Email.delete(data)
    return redirect('/email/display')

# '/user/new' -> display the route with the form
# '/user/create' -> process the form from above
# '/user/<int:id>' -> display the user's info -> Show
# '/user/<int:id>/edit' -> display the user's info in a form so that they can edit it
# '/user/<int:id>/update' -> process the edit form
# '/user/<int:id>/delete' -> delete the user at that id