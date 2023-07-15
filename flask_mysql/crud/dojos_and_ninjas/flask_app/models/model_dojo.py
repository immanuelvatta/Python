# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
#avoid circular import, dont import class, but import file
from flask_app.models import model_ninja
# model the class after the users table from  database
class Dojo:
    DB = 'dojos_ninjas_db'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    #TODO CREATE
    #* the save method will be used when we need to save a new user to our database
    @classmethod
    def create(cls, data):
        """
        This function takes in a data dictionary and create a row in our database and 
        returns an int which is the new row's id value
        
        This if successful add user to database and returns the new row's id
        """
        query = """INSERT INTO dojos (name)
                VALUES (%(name)s);"""
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result
    
    #TODO READ
    #*the get_all method will be used when we need to retrieve all the rows of the table dojos
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM dojos;"""
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for dict in results:
            dojos.append(cls(dict))
        return dojos
    
    #* the get_one method will be used when we need to retrieve just one specific row of the table dojos
    @classmethod
    def get_one(cls,data):
        query = """SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"""
        # data = {'id':id}
        results = connectToMySQL(DATABASE).query_db(query,data)#list of dictionaries
        dict = results[0] # take first result out of the list
        dojo_instance = cls(dict) # new instance of Dealer class from a dictionary
        dojo_instance.all_ninjas = [] # taking an empty list and assigning it to dojo_instance.all_ninjas
        if dict['ninjas.id'] != None : #if check to see if dictionary with this key is empty, then 
        #! if there is no cars.id then there are no cars
            # if there is something in ninjas.id (at least one ninja) then every other row a new ninja and it is associated to the same dojo
            for ninja_dict in results:
                #ninja_dict is going to hold a dictionary (all the dojo info, all the ninja info (for a singular ninja))
                ninja_data = {
                    #setting the specific data from car_dict you wanted 
                    #all conflicting columns
                    'id': ninja_dict['ninjas.id'],
                    'created_at' : ninja_dict['ninjas.created_at'],
                    'updated_at' : ninja_dict['ninjas.updated_at'],
                    #all the rest of the columns
                    'first_name' : ninja_dict['first_name'],
                    'last_name' : ninja_dict['last_name'],
                    'age' : ninja_dict['age'],
                    'dojo_id' : ninja_dict['dojo_id']
                }
                ninja_instance = model_ninja.Ninja(ninja_data) # creating an instance of ninja  #!make sure you import the file model_ninja
                dojo_instance.all_ninjas.append(ninja_instance) #populating the list that we assigned to the instance 
                # now we have an individual list of car class objects (instances)  # now we have an individual list of car class objects (instances) 
        return dojo_instance 
    
    
    #TODO UPDATE
    #* the update method will be used when we need to update a dojo in our database
    @classmethod
    def update(cls,data):
        query = """UPDATE dojos 
                SET name = %(name)s, updated_at = CURRENT_TIMESTAMP 
                WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    #TODO DELETE
    #* the delete method will be used when we need to delete a dojo from our database
    @classmethod
    def delete(cls,data):
        query = """DELETE FROM dojos WHERE id = %(id)s;"""
        # data = {'id': id}
        return connectToMySQL(DATABASE).query_db(query,data)