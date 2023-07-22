# import the function that will return an instance of a connection
#       folder  folder  file                    function
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE , bcrypt
from flask import flash, session

from flask_app.models import model_user
# from flask_app.models import model_user

class Recipe:
    
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    #TODO CREATE
    #* the save method will be used when we need to save a new user to our database
    @classmethod
    def create(cls, data):
        """
        This if successful add user to database and returns the new row's id
        """
        query = """INSERT INTO recipes (user_id, name, description, instructions, date_made, under_30)
                VALUES (%(user_id)s, %(name)s,%(description)s,%(instructions)s, %(date_made)s, %(under_30)s);"""
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result
    
    #TODO READ
    #*the display_all_users method will be used when we need to retrieve all the rows of the table user
    @classmethod
    def get_all(cls):
        """
        Function doesn't take in anything but returns a list of instances of dealers
        """
        query = """SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"""
        #what is results?  list !! list of what? dictionaries
        results = connectToMySQL(DATABASE).query_db(query)
        # print(results)
        all_recipes = [] #list
        
        for user_dict in results:
            recipe_instance = cls(user_dict) # new instance of Recipe class from a dictionary (represents a new recipe)
            user_data = {
                'id' : user_dict['users.id'],
                'created_at' : user_dict['users.created_at'],
                'updated_at' : user_dict['users.updated_at'],
                'first_name' : user_dict['first_name'],
                'last_name' : user_dict['last_name'],
                'email' : user_dict['email'],
                'password' : user_dict['password']
            }
            user_instance = model_user.User(user_data) #creating an instance of user
            recipe_instance.user = user_instance 
            all_recipes.append(recipe_instance) #populating the list that we assigned to the instance
        return all_recipes
    
    @classmethod
    def get_one(cls,id):
        query = """SELECT * FROM recipes WHERE id = %(id)s;"""
        # data = {'id':id}
        
        results = connectToMySQL(DATABASE).query_db(query,{'id': id})
        return cls(results[0])
    
    @classmethod
    def get_one_recipe(cls,id):
        query = """SELECT * FROM recipes JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(id)s;"""
        # data = {'id':id}
        #fix users id (extract the data) secondary table to its own instance
        results = connectToMySQL(DATABASE).query_db(query,{'id': id})
        if not results:
            return []
        dictionary = results[0]
        recipe_instance = cls(dictionary) #each recipe is only 
        # recipe_instance.all_users = []
        # in this instance its not really applicable 
        if dictionary['users.id'] != None:
            
            for user_dict in results:
                user_data = {
                    # 'first_name' : user_dict['first_name'],
                    # 'last_name' : user_dict['last_name'],
                    # 'email' : user_dict['email'],
                    # 'password' : user_dict['password'],
                    **user_dict, #! same as first_name, lastname, email, password getting added
                    'id' : user_dict['users.id'],
                    'created_at' : user_dict['users.created_at'],
                    'updated_at' : user_dict['users.updated_at']
                }
                user_instance = model_user.User(user_data)
                #recipe_instance.all_users.append(user_instance) for get all
                recipe_instance.user = user_instance
        return recipe_instance
    
    @classmethod
    def update(cls, data):
        query = """UPDATE recipes 
                SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, under_30 = %(under_30)s
                WHERE id = %(id)s;"""
                
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def delete(cls, id):
        query = """DELETE FROM recipes WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, {"id": id})
    
    @staticmethod
    def recipe_validator(data):
        is_valid = True
        print(data)
        if len(data['name']) < 3:
            flash("Recipe name should be at least 3 characters", 'err_recipe_name')
            is_valid = False
        
        if len(data['description']) < 3:
            flash("Recipe description should be at least 3 characters", 'err_recipe_description')
            is_valid = False
        if len(data['instructions']) < 3:
            flash("Recipe Instructions should be at least 3 characters", 'err_recipe_instructions')
            is_valid = False
        if 'under_30' not in data:
            flash("Needs to be checked", 'err_recipe_under_30')
            is_valid = False 
        
        if len(data['date_made']) < 1:
            flash ("Invalid Date",'err_recipe_date_made')
        return is_valid