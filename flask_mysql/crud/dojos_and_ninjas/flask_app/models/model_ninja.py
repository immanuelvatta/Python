# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
# model the class after the users table from  database
class Ninja:
    # DB = 'dojos_ninjas_db'
    def __init__(self, data):
        self.id = data['id']
        self.dojo_id = data["dojo_id"]
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    #TODO CREATE
    #* the save method will be used when we need to save a new ninja to our database
    @classmethod
    def create(cls, data):
        """
        This function takes in a data dictionary and create a row in our database and 
        returns an int which is the new row's id value
        
        This if successful add user to database and returns the new row's id
        """
        query = """INSERT INTO ninjas (dojo_id, first_name, last_name, age)
                VALUES (%(dojo_id)s,%(first_name)s, %(last_name)s,%(age)s);"""
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result
    
    #TODO READ
    #*the get_all method will be used when we need to retrieve all the rows of the table ninjas
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM ninjas;"""
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for dict in results:
            users.append(cls(dict))
        return users
    
    #* the get_one method will be used when we need to retrieve just one specific row of the table ninjas
    @classmethod
    def get_one(cls,data):
        query = """SELECT * FROM ninjas WHERE id = %(id)s;"""
        # data = {'id':id}
        results = connectToMySQL(DATABASE).query_db(query,data)
        return cls(results[0])
    
    
    #TODO UPDATE
    #* the update method will be used when we need to update a ninja in our database
    @classmethod
    def update(cls,data):
        query = """UPDATE ninjas 
                SET dojo_id = %(dojo_id)s, first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, updated_at = CURRENT_TIMESTAMP 
                WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    #TODO DELETE
    #* the delete method will be used when we need to delete a ninja from our database
    @classmethod
    def delete(cls,data):
        query = """DELETE FROM ninjas WHERE id = %(id)s;"""
        # data = {'id': id}
        return connectToMySQL(DATABASE).query_db(query,data)