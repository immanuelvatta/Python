# import the function that will return an instance of a connection
#       folder  folder  file                    function
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re # the regex module
# model the class after the users table from  database

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    # should change db based on schema you're trying to access
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    #TODO CREATE
    #* the save method will be used when we need to save a new user to our database
    @classmethod
    def create(cls, data):
        """
        This if successful add user to database and returns the new row's id
        """
        query = """INSERT INTO emails (email)
                VALUES (%(email)s);"""
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result
    
    #TODO READ
    #*the display_all_users method will be used when we need to retrieve all the rows of the table user
    @classmethod
    def get_all(cls):
        """
        Function doesn't take in anything but returns a list of instances of dealers
        """
        query = """SELECT * FROM emails;"""
        #what is results?  list !! list of what? dictionaries
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        #transform the list of dictionaries -> a list of object/instances
        for dict in results:
            users.append(cls(dict))
        return users
    
    #* the get_one method will be used when we need to retrieve just one specific row of the table
    @classmethod
    def get_one(cls,data):
        query = """SELECT * FROM emails WHERE id = %(id)s;"""
        # data = {'id':id}
        results = connectToMySQL(DATABASE).query_db(query,data)
        return cls(results[0])
    
    #TODO UPDATE
    #* the update method will be used when we need to update a user in our database
    @classmethod
    def update(cls,data):
        query = """UPDATE emails 
                SET email = %(email)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    #TODO DELETE
    #* the delete method will be used when we need to delete a user from our database
    @classmethod
    def delete(cls,data):
        """
        This function takes in a dictionary containing a key of 'id' and value that is the int representation of the id you want to delete
        """
        query = """DELETE FROM emails WHERE id = %(id)s;"""
        # data = {'id': id}
        #returns nothing
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @staticmethod
    def is_valid_email(data):
        is_valid = True
        query = """SELECT * FROM emails WHERE email = %(email)s;"""
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len (results) >= 1:
            flash ('***Email EXISTS***')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash('***Invalid email***')
            is_valid = False
        return is_valid