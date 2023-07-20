from flask import flash, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import model_patient
from flask_app import DATABASE, bcrypt
class Hospital:
    def __init__(self, data:dict):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.name = data['name']
        self.city = data['city']
        self.password = data['password']
        
        
    #classmethods
    #C
    @classmethod
    def create(cls,data:dict):
        query = "INSERT INTO hospitals (name,city,password) VALUES (%(name)s, %(city)s, %(password)s)"
        hospital_id = connectToMySQL(DATABASE).query_db(query,data)
        return hospital_id
    #R
    @classmethod
    def get_one_by_name(cls,data:dict):
        query = "SELECT * FROM hospitals where name = %(name)s"
        #what datatype does this return -> list ... of dictionary (only one) || on fail will return False or if empty will return []
        results = connectToMySQL(DATABASE).query_db(query,data)
        
        # protect against bad request
        if not results:
            return False
        
        # this one dictionary convert it into an instance and return that instance
        return cls(results[0])
    
    @classmethod
    def get_one(cls,data:dict):
        # query = "SELECT * FROM hospitals where id = %(id)s"
        query = "SELECT * FROM hospitals JOIN patients ON patients.hospital_id = hospitals.id WHERE hospitals.id = %(id)s;"
        #what datatype does this return -> list ... of dictionary (only one) || on fail will return False or if empty will return []
        results = connectToMySQL(DATABASE).query_db(query,data)
        # protect against bad request
        if not results:
            return False
        
        # this one dictionary convert it into an instance and return that instance
        hospital_instance =  cls(results[0])
        
        #obj/instances work like dictionaries where if the attribute doesn't exist then it will create it, but if it does exist then it will update it.
        hospital_instance.patients = []
        
        
        if results[0]['patients.id'] != None:
            for dict in results:
                patient_data = {
                    #conflict columns
                    #id, created_at, updated_at
                    'id': dict['patients.id'],
                    'created_at': dict['patients.created_at'],
                    'updated_at': dict['patients.updated_at'],
                    
                    #all the rest of the columns
                    # **dict,
                    'first_name' : dict['first_name'],
                    'last_name' : dict['last_name'],
                    'age' : dict['age'],
                    'gender' : dict['gender'],
                    'hospital_id' : dict['hospital_id']
                }
                # create an instance of the patient -> need to import class
                patient_instance = model_patient.Patient(patient_data)
                hospital_instance.patients.append(patient_instance)
        return hospital_instance
    #U
    @classmethod
    def update_one(cls, data:dict):
        query = "UPDATE hospitals SET name = %(name)s, city = %(city)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
    #D
    @classmethod
    def delete_one(cls,data:dict):
        query = "DELETE FROM hospitals WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query,data)
    
    #staticmethod
    @staticmethod
    def validate(data:dict):
        is_valid = True
        
        if len(data['name']) < 1:
            is_valid = False
            flash("Invalid Name", 'err_hospital_name')
        if len(data['city']) < 1:
            is_valid = False
            flash("Invalid City", 'err_hospital_city')
        if len(data['password']) < 1:
            is_valid = False
            flash("Invalid Password", 'err_hospital_password')
        
        if is_valid:
            potential_hospital = Hospital.get_one_by_name({'name': data['name']})
            
            if potential_hospital:
                is_valid = False
                flash("Name already exists", 'err_hospital_name')
                    
        return is_valid
    
    #staticmethod
    @staticmethod
    def validate_update(data:dict):
        is_valid = True
        
        if len(data['name']) < 1:
            is_valid = False
            flash("Invalid Name", 'err_hospital_name')
        if len(data['city']) < 1:
            is_valid = False
            flash("Invalid City", 'err_hospital_city')
        
        return is_valid
        
        
    #staticmethod
    @staticmethod
    def validate(data:dict):
        is_valid = True
        
        if len(data['name']) < 1:
            is_valid = False
            flash("Invalid Name", 'err_hospital_name')
        if len(data['city']) < 1:
            is_valid = False
            flash("Invalid City", 'err_hospital_city')
        if len(data['password']) < 1:
            is_valid = False
            flash("Invalid Password", 'err_hospital_password')
        
        if is_valid:
            potential_hospital = Hospital.get_one_by_name({'name': data['name']})
            
            if potential_hospital:
                is_valid = False
                flash("Name already exists", 'err_hospital_name')
                    
        return is_valid
    
    @staticmethod
    def validate_login(data):
        is_valid = True
            
        if len(data['name']) < 1:
            is_valid = False
            flash("Invalid Name", 'err_hospital_name')
        if len(data['password']) < 1:
            is_valid = False
            flash("Invalid Password", 'err_hospital_password')
            
        if is_valid == True:
            potential_hospital = Hospital.get_one_by_name({'name': data['name']})
            
            #if potential Hospital is not in database -> bad name
            if not potential_hospital:
                is_valid = False
                flash("Invalid Credentials",'err_hospital_name')
            else:
                #compare the password given with the bcrypt password
                has_passed = bcrypt.check_password_hash(potential_hospital.password, data['password'])
                if not has_passed:
                    is_valid = False
                    flash("Invalid Credentials",'err_hospital_password')
                else:
                    session['hospital_id'] = potential_hospital.id
        return is_valid