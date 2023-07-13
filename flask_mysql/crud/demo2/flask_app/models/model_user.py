from flask_app.config.mysqlconnection import MySQLConnection
from flask_app import DATABASE


class User:
    def __init__(self, data:dict):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        
        
    @classmethod
    def get_one(cls, data:dict):
                                    #       key in data dict
        query = "SELECT * FROM users WHERE %(id)s"

        results = MySQLConnection(DATABASE).query_db(query, data) # list of dictionaries
        
        return cls(results[0])
    #5 core class methods
    
    # create/save
    # get_all
    # get_one
    # update
    # delete