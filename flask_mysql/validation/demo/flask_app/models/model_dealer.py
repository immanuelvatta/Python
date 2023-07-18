#       folder  folder  file                    function
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import bcrypt
from flask import flash, session
import re # the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


DATABASE = 'july_car_dealer_2023_db'
#avoid circular import, dont import class, but import file
from flask_app.models import model_car
class Dealer:
    
    def __init__(self, data:dict):
        self.id = data['id']
        self.location = data['location']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.password = data['password']
        self.email = data['email']
        
        
    #C
    @classmethod
    def create(cls, data:dict) :
        """this function takes in a data dictionary and create a row in our database and returns an int which is the new row's id value
        """
        #query
        query = "INSERT INTO dealers (location,name, email, password) VALUES (%(location)s, %(name)s , %(email)s , %(password)s);"
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
    
    @classmethod
    def get_one_by_email(cls,data):
        query = "SELECT * FROM dealers WHERE dealers.email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        
        #results = [] -> falsy
        if not results:
            return False
        
        dict = results[0]
        dealer_instance = cls(dict)
        
        return dealer_instance
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dealers LEFT JOIN cars ON cars.dealer_id = dealers.id WHERE dealers.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data) #list of dictionaries
        # print(results)
        dict = results[0] # take first result out of the list
        dealer_instance = cls(dict) # new instance of Dealer class from a dictionary
        dealer_instance.all_cars = [] # taking an empty list and assigning it to dealer_instance.all_cars
        if (dict['cars.id'] != None): #if check to see if dictionary with this key is empty, then 
            #! if there is no cars.id then there are no cars
            # if there is something in cars.id (at least one car) then every other row a new car and it is associated to the same dealer
            for car_dict in results:
                # print(car_dict)
                #car_dict is going to hold a dictionary (all the dealer info, all the car info (for a singular car))
                car_data = {
                    #setting the specific data from car_dict you wanted 
                    #all conflicting columns
                    'id' : car_dict['cars.id'],
                    'created_at' : car_dict['cars.created_at'],
                    'updated_at' : car_dict['cars.updated_at'],
                    
                    #all the rest of the columns
                    'make' : car_dict['make'],
                    'model' : car_dict['model'],
                    'year' : car_dict['year']
                }
                car_instance = model_car.Car(car_data) # creating an instance of car  #!make sure you import the file model_car
                dealer_instance.all_cars.append(car_instance) #populating the list that we assigned to the instance 
                # now we have an individual list of car class objects (instances) 
            # print()
        return dealer_instance
    #U
    #D
    @classmethod
    def delete_one(cls, data:dict): 
        """
        This function takes in a dictionary containing a key of 'id' and value that is the int representation of the id you want to delete
        """
        query = "DELETE FROM dealers WHERE id = %(id)s;"
        #results = nothing
        results = connectToMySQL(DATABASE).query_db(query,data)
        return results
    
    @staticmethod
    #data:dict => request.form from the controller file -> html page
    def validator(data:dict):
        """
        This method takes in a dictionary from the HTML page (usually request form) and checks 
        each of the keys in that dictionary and sees if they match the requirement. 
        If they dont then the validator will return false (meaning it is not valid) 
        and if it does then it will return true (meaning it is valid)
        """
        is_valid = True
    
        if len(data['email']) < 5:
            print("****ERR email****")
            # session['erremail'] = "****ERR email bad****"
            flash("****ERR email****")
            flash("****ERR email****", 'err_dealer_email')
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False
        
        if len(data['password']) < 8:
            print("****ERR password****")
            flash("****ERR password****")
            flash("****ERR password****", 'err_dealer_password')
            is_valid = False
        
        return is_valid
    
    @staticmethod
    def validator_login(data:dict):
        """
        This method takes in a dictionary from the HTML page (usually request form) and checks 
        each of the keys in that dictionary and sees if they match the requirement. 
        If they dont then the validator will return false (meaning it is not valid) 
        and if it does then it will return true (meaning it is valid)
        """
        is_valid = True
    
        if len(data['email']) < 5:
            print("****ERR email****")
            # session['erremail'] = "****ERR email bad****"
            flash("****ERR email****")
            flash("****ERR email****", 'err_dealer_email')
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False
        
        if len(data['password']) < 8:
            print("****ERR password****")
            flash("****ERR password****")
            flash("****ERR password****", 'err_dealer_password')
            is_valid = False
            
        if is_valid == True:
            potential_user = Dealer.get_one_by_email({'email': data['email']})
            if not potential_user:
                is_valid = False
                flash("Invalid","err_dealer_email")
            else:
                #compare the password in the database with the password in the "data" dictionary 
                output = bcrypt.check_password_hash(potential_user.password, data['password'])
                print(f"******{output}********")
                if output == False:
                    is_valid = False
                    flash("Invalid","err_dealer_password")
                
                else:
                    session['dealer_id'] = potential_user.id
                    print("***SESSION HAS BEEN SET****")
        return is_valid