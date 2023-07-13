#       folder  folder  file                    function
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'july_car_dealer_2023_db'

class Car:
    
    def __init__(self, data:dict):
        self.id = data['id']
        self.make = data['make']
        self.model = data['model']
        self.year = data['year']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
        
    #C
    @classmethod
    def create(cls, data:dict) :
        """this function takes in a data dictionary and create a row in our database and returns an int which is the new row's id value

        Args:
            data (_type_): _description_
        """
        #query
        query = "INSERT INTO cars (make,model,year, dealer_id) VALUES (%(make)s, %(model)s, %(year)s , %(dealer_id)s);"
        #contact the DB
        id = connectToMySQL(DATABASE).query_db(query,data)
        #return
        return id
    #R
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cars;"
        """
        Function doesn't take in anything but returns a list of instances of dealers
        """
        #what is results?  list !! list of what? dictionaries
        results = connectToMySQL(DATABASE).query_db(query)
        
        #transform the list of dictionaries -> a list of object/instances
        all_cars = []
        
        for dictionary in results:
            instance = cls(dictionary)
            all_cars.append(instance)
        return all_cars
    #U
    #D
    @classmethod
    def delete_one(cls, data:dict): 
        """
        This function takes in a dictionary containing a key of 'id' and value that is the int representation of the id you want to delete
        """
        query = "DELETE FROM cars WHERE it = %(id)s;"
        #results = nothing
        results = connectToMySQL(DATABASE).query_db(query,data)
        return results