# import the function that will return an instance of a connection
#       folder  folder  file                    function
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
# model the class after the users table from  database
class Survey:
    # should change db based on schema you're trying to access
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    #TODO CREATE
    #* the save method will be used when we need to save a new user to our database
    @classmethod
    def create(cls, data):
        """
        This if successful add user to database and returns the new row's id
        """
        query = """INSERT INTO dojos (name, location, language,comment)
                VALUES (%(name)s, %(location)s,%(language)s,%(comment)s);"""
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result
    
    #TODO READ
    #*the display_all_users method will be used when we need to retrieve all the rows of the table user
    @classmethod
    def get_all(cls):
        """
        Function doesn't take in anything but returns a list of instances of dealers
        """
        query = """SELECT * FROM dojos;"""
        #what is results?  list !! list of what? dictionaries
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        #transform the list of dictionaries -> a list of object/instances
        for dict in results:
            users.append(cls(dict))
        return users
    
    #* the get_one method will be used when we need to retrieve just one specific row of the table
    @classmethod
    def get_one(cls):
        query = """SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"""
        # data = {'id':id}
        results = connectToMySQL(DATABASE).query_db(query)
        return cls(results[0])
    
    
    #TODO UPDATE
    #* the update method will be used when we need to update a user in our database
    @classmethod
    def update(cls,data):
        query = """UPDATE dojos 
                SET name = %(name)s, location = %(location)s, language = %(language)s, comment = %(comment)s , updated_at = CURRENT_TIMESTAMP 
                WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    #TODO DELETE
    #* the delete method will be used when we need to delete a user from our database
    @classmethod
    def delete(cls,data):
        """
        This function takes in a dictionary containing a key of 'id' and value that is the int representation of the id you want to delete
        """
        query = """DELETE FROM dojos WHERE id = %(id)s;"""
        # data = {'id': id}
        #returns nothing
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @staticmethod
    def is_valid_survey(data):
        is_valid = True
        if len(data['name']) <= 2:
            is_valid = False
            flash('***Invalid Name***')
        if len(data['location']) < 1:
            is_valid = False
            flash('***Invalid location: must choose one***')
        if len(data['language']) < 1:
            is_valid = False
            flash('***Invalid language: must choose one***')
        if len(data['comment']) <= 2:
            is_valid = False
            flash('***Invalid comment: Too Short***')
        return is_valid