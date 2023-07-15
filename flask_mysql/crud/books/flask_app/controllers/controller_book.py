from flask_app import app
from flask import redirect, render_template,request

from flask_app.models.model_author import Author
from flask_app.models.model_book import Book


#fills out the form 
@app.route('/book/new')
def author_new():
    all_books = Book.get_all()
    return render_template('books.html', all_books = all_books)

#process  the form
@app.route('/book/create', methods=['POST'])
def book_create():
    #do the creating
    data = {
        ** request.form
    }
    Book.save(data)
    return redirect('/book/new')


@app.route('/book/<int:id>')
def book_show(id):
    data = {
        "id": id
    }
    book = Book.get_one(data)
    return render_template("book_show.html",book = book)

@app.route('/book/<int:id>/edit')
def book_edit(id):
    return render_template("book_edit.html")

@app.route('/book/<int:id>/update', methods=['POST'])
def book_update(id):
    return redirect('/')

@app.route('/book/<int:id>/delete')
def book_delete(id):
    return redirect('/')

# '/user/new' -> display the route with the form
# '/user/create' -> process the form from above
# '/user/<int:id>' -> display the user's info -> Show
# '/user/<int:id>/edit' -> display the user's info in a form so that they can edit it
# '/user/<int:id>/update' -> process the edit form
# '/user/<int:id>/delete' -> delete the user at that id