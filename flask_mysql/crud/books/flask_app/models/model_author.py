# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
# model the class after the users table from  database
from flask_app.models import model_book
class Author:
    # DB = ''
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    #TODO CREATE
    #* the save method will be used when we need to save a new authors to our database
    @classmethod
    def create(cls, data):
        """
        This function takes in a data dictionary and create a row in our database and 
        returns an int which is the new row's id value
        
        This if successful add user to database and returns the new row's id
        """
        query = """INSERT INTO authors (name) VALUES (%(name)s);"""
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result
    
    @classmethod
    def add_favorite(cls,data):
        query = """INSERT INTO favorites (author_id,book_id) VALUES (%(author_id)s,%(book_id)s);"""
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result
    
    #TODO READ
    #*the get_all method will be used when we need to retrieve all the rows of the table authors
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM authors;"""
        results = connectToMySQL(DATABASE).query_db(query)
        authors = []
        for dict in results:
            authors.append(cls(dict))
        return authors
    
    #* the get_one method will be used when we need to retrieve just one specific row of the table authors
    @classmethod
    def get_one(cls,data):
        query = """SELECT * FROM authors WHERE id = %(id)s;"""
        # data = {'id':id}
        results = connectToMySQL(DATABASE).query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def get_by_id(cls,data):
        query = """SELECT * FROM authors 
                LEFT JOIN favorites ON authors.id = favorites.author_id 
                LEFT JOIN books ON books.id = favorites.book_id 
                WHERE authors.id = %(id)s;"""
        results = connectToMySQL('books').query_db(query,data)

        # Creates instance of author object from row one
        author = cls(results[0])
        # append all book objects to the instances favorites list.
        for row in results:
            # if there are no favorites
            if row['books.id'] == None:
                break
            # common column names come back with specific tables attached
            data = {
                "id": row['books.id'],
                "title": row['title'],
                "num_of_pages": row['num_of_pages'],
                "created_at": row['books.created_at'],
                "updated_at": row['books.updated_at']
            }
            author.favorite_books.append(model_book.Book(data))
        return author
    
    
    #TODO UPDATE
    #* the update method will be used when we need to update a authors in our database
    @classmethod
    def update(cls,data):
        query = """UPDATE authors 
                SET name = %(name)s, updated_at = CURRENT_TIMESTAMP 
                WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    #TODO DELETE
    #* the delete method will be used when we need to delete a authors from our database
    @classmethod
    def delete(cls,data):
        query = """DELETE FROM authors WHERE id = %(id)s;"""
        # data = {'id': id}
        return connectToMySQL(DATABASE).query_db(query,data)