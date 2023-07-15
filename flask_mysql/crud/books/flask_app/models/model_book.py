# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import model_author
# model the class after the users table from  database
class Book:
    # DB = ''
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    #TODO CREATE
    #* the save method will be used when we need to save a new books to our database
    @classmethod
    def create(cls, data):
        """
        This function takes in a data dictionary and create a row in our database and 
        returns an int which is the new row's id value
        
        This if successful add user to database and returns the new row's id
        """
        query = """INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);"""
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result
    
    #TODO READ
    #*the get_all method will be used when we need to retrieve all the rows of the table books
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM books;"""
        results = connectToMySQL(DATABASE).query_db(query)
        books = []
        for dict in results:
            books.append(cls(dict))
        return books
    
    #* the get_one method will be used when we need to retrieve just one specific row of the table books
    @classmethod
    def get_one(cls,data):
        query = """SELECT * FROM books WHERE id = %(id)s;"""
        # data = {'id':id}
        results = connectToMySQL(DATABASE).query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def get_by_id(cls,data):
        query = """SELECT * FROM books 
                LEFT JOIN favorites ON books.id = favorites.book_id 
                LEFT JOIN authors ON authors.id = favorites.author_id 
                WHERE books.id = %(id)s;"""
        results = connectToMySQL('books').query_db(query,data)

        book = cls(results[0])

        for row in results:
            if row['authors.id'] == None:
                break
            data = {
                "id": row['authors.id'],
                "name": row['name'],
                "created_at": row['authors.created_at'],
                "updated_at": row['authors.updated_at']
            }
            book.authors_who_favorited.append(model_author.Author(data))
        return book

    
    
    #TODO UPDATE
    #* the update method will be used when we need to update a books in our database
    @classmethod
    def update(cls,data):
        query = """UPDATE books 
                SET title = %(title)s, num_of_pages = %(num_of_pages)s ,updated_at = CURRENT_TIMESTAMP 
                WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    #TODO DELETE
    #* the delete method will be used when we need to delete a books from our database
    @classmethod
    def delete(cls,data):
        query = """DELETE FROM books WHERE id = %(id)s;"""
        # data = {'id': id}
        return connectToMySQL(DATABASE).query_db(query,data)