# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the users table from  database
class User:
    DB = 'users_db'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.full_name = f'{self.first_name} {self.last_name}'
        
    #TODO CREATE
    #* the save method will be used when we need to save a new user to our database
    @classmethod
    def create(cls, data):
        """
        This if successful add user to database and returns the new row's id
        """
        query = """INSERT INTO users (first_name, last_name, email)
                VALUES (%(first_name)s, %(last_name)s,%(email)s);"""
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    
    #TODO READ
    #*the display_all_users method will be used when we need to retrieve all the rows of the table user
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM users;"""
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for dict in results:
            users.append(cls(dict))
        return users
    
    #* the get_one method will be used when we need to retrieve just one specific row of the table
    @classmethod
    def get_one(cls,data):
        query = """SELECT * FROM users WHERE id = %(id)s;"""
        # data = {'id':id}
        results = connectToMySQL(cls.DB).query_db(query,data)
        return cls(results[0])
    
    
    #TODO UPDATE
    #* the update method will be used when we need to update a user in our database
    @classmethod
    def update(cls,data):
        query = """UPDATE users 
                SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = CURRENT_TIMESTAMP 
                WHERE id = %(id)s;"""
        return connectToMySQL(cls.DB).query_db(query,data)
    
    #TODO DELETE
    #* the delete method will be used when we need to delete a user from our database
    @classmethod
    def delete(cls,data):
        query = """DELETE FROM users WHERE id = %(id)s;"""
        # data = {'id': id}
        return connectToMySQL(cls.DB).query_db(query,data)