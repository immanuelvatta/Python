#       folder  folder  file                    function
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'july_car_dealer_2023_db'

class Dealer:
    
    def __init__(self, data:dict):
        self.id = data['id']
        self.location = data['location']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
        
    #C
    @classmethod
    def create(cls, data:dict) :
        """this function takes in a data dictionary and create a row in our database and returns an int which is the new row's id value
        """
        #query
        query = "INSERT INTO dealers (location,name) VALUES (%(location)s, %(name)s);"
        #contact the DB
        id = connectToMySQL(DATABASE).query_db(query,data)
        #return
        return id
    #R
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dealers;"
        """
        Function doesnt take in anything but returns a list of instances of dealers
        """
        #what is results?  list !! list of what? dictionaries
        results = connectToMySQL(DATABASE).query_db(query)
        
        #transform the list of dictionaries -> a list of object/instances
        all_dealers = []
        
        for dictionary in results:
            instance = cls(dictionary)
            all_dealers.append(instance)
        return all_dealers
    #U
    #D
    @classmethod
    def delete_one(cls, data:dict): 
        """
        This function takes in a dictionary containing a key of 'id' and value that is the int representation of the id you want to delete
        """
        query = "DELETE FROM dealers WHERE it = %(id)s;"
        #results = nothing
        results = connectToMySQL(DATABASE).query_db(query,data)
        return results