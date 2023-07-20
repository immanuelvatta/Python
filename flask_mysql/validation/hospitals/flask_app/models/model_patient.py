from flask import flash, session
from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import DATABASE, bcrypt
class Patient:
    def __init__(self, data:dict):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.gender = data['gender']
        self.hospital_id = data['hospital_id']
        self.full_name = f"{self.first_name.capitalize()} {self.last_name.capitalize()}"
        
        
    #classmethods
    #C
    @classmethod
    def create(cls,data:dict):
        query = "INSERT INTO patients (first_name,last_name,age, gender, hospital_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(gender)s, %(hospital_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)
    #R
    @classmethod
    def get_one_by_name(cls,data:dict):
        query = "SELECT * FROM patients where name = %(name)s"
        #what datatype does this return -> list ... of dictionary (only one) || on fail will return False or if empty will return []
        results = connectToMySQL(DATABASE).query_db(query,data)
        
        # protect against bad request
        if not results:
            return False
        
        # this one dictionary convert it into an instance and return that instance
        return cls(results[0])
    
    @classmethod
    def get_one(cls,data:dict):
        query = "SELECT * FROM patients where id = %(id)s"
        #what datatype does this return -> list ... of dictionary (only one) || on fail will return False or if empty will return []
        results = connectToMySQL(DATABASE).query_db(query,data)
        print("---------------")
        print(results)
        # protect against bad request || if results == falsy value -> () or False
        if not results:
            return False
        
        # this one dictionary convert it into an instance and return that instance
        return cls(results[0])
    #U
    @classmethod
    def update_one(cls, data:dict):
        query = "UPDATE hospitals SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s WHERE id, gender = %(gender)s = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
    #D
    @classmethod
    def delete_one(cls,data:dict):
        query = "DELETE FROM patients WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query,data)
    

    #staticmethod
    @staticmethod
    def validate(data:dict):
        is_valid = True
        
        if len(data['first_name']) < 1:
            is_valid = False
            flash("Invalid first", 'err_patient_first_name')
        if len(data['last_name']) < 1:
            is_valid = False
            flash("Invalid last_name", 'err_patient_last_name')
        if int(data['age']) < 1:
            is_valid = False
            flash("Invalid Age", 'err_patient_age')
        if len(data['gender']) < 1:
            is_valid = False
            flash("Invalid Password", 'err_patient_gender')
        
        return is_valid
    
