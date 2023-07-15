from flask_app import app
from flask import redirect, render_template,request

from flask_app.models.model_author import Author
from flask_app.models.model_book import Book


#fills out the form 
@app.route('/author/new')
def author_new():
    all_authors = Author.get_all()
    return render_template('authors.html', all_authors = all_authors)

#process  the form
@app.route('/author/create', methods=['POST'])
def author_create():
    #do the creating
    data = {
        ** request.form
    }
    Author.save(data)
    return redirect('/author/new')


@app.route('/author/<int:id>')
def author_show(id):
    data = {
        "id": id
    }
    author = Author.get_one(data)
    return render_template("author_show.html",author = author)

@app.route('/author/<int:id>/edit')
def author_edit(id):
    return render_template("author_edit.html")

@app.route('/author/<int:id>/update', methods=['POST'])
def author_update(id):
    return redirect('/')

@app.route('/author/<int:id>/delete')
def author_delete(id):
    return redirect('/')

# '/user/new' -> display the route with the form
# '/user/create' -> process the form from above
# '/user/<int:id>' -> display the user's info -> Show
# '/user/<int:id>/edit' -> display the user's info in a form so that they can edit it
# '/user/<int:id>/update' -> process the edit form
# '/user/<int:id>/delete' -> delete the user at that id