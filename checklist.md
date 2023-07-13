# Pre-checklist install
installing pipenv on a global scope


`!Only needs to be done once!`

```console
pip install pipenv
``` 

# Start of checklist
- Create a folder for our new assignment
- go into that folder
- create the virtual env with flask

```console
pipenv install flask PyMySQL
```
- WARNING! Make sure pipfile & pipfile.lock are there!! If not FIX THIS NOW!!!
- activate virtual env
```console
pipenv shell
```

---
- Create folder structure
```
- flask_app(📂)
    - config (📂)
        - mysqlconnection.py(📜)
    - controllers (📂)
        # You will have a controller file for every table table in your database
        -controller_user.py(📜)
    - models (📂)
        # You will have a model file for every table in your database
        model_user.py(📜)
    - static (📂)
        - css(📂)
            - styles.css (📃)
        - img (📁)
        - js(📂)
            - script.js (📃)
    - templates (📂)
        - index.html (📄)
    - __init__.py (📜)
- pipfile(📄)
- pipfile.lock(📄)
- server.py(📜)
```

## Create server.py

```Py
from flask_app import app

#TODO import controllers

#MAKE SURE THIS IS AT THE BOTTOM
if __name__=="__main__":
    app.run(debug=True)
```
- Create templates folder
- add index.html in templates folder
- Test it out

## Create mysqlconnection.py file

```PY
# a cursor is the object we use to interact with the database
import pymysql.cursors
# this class will give us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
        # change the user and password as needed
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root', 
                                    password = 'root', 
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = False)
        # establish the connection to the database
        self.connection = connection
    # the method to query the database
    def query_db(self, query:str, data:dict=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
                cursor.execute(query)
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
                # if the query fails the method will return FALSE
                print("Something went wrong", e)
                return False
            finally:
                # close the connection
                self.connection.close() 
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)
```

## create model file
- change this file based on your table in db
    - each model has its own controller
```PY
# import the function that will return an instance of a connection
#       folder  folder  file                    function
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the users table from  database
class User:
    # should change db based on schema you're trying to access
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
        """
        Function doesn't take in anything but returns a list of instances of dealers
        """
        query = """SELECT * FROM users;"""
        #what is results?  list !! list of what? dictionaries
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        #transform the list of dictionaries -> a list of object/instances
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
        """
        This function takes in a dictionary containing a key of 'id' and value that is the int representation of the id you want to delete
        """
        query = """DELETE FROM users WHERE id = %(id)s;"""
        # data = {'id': id}
        #returns nothing
        return connectToMySQL(cls.DB).query_db(query,data)
```

## create controller.py file
- each controller has its own model
    - don't forget to import models
```PY
from flask_app import app

from flask import render_template, redirect


#fills out the form 
@app.route('/user/new')
def user_new():
    return render_template('user_new.html')

#process  the form
@app.route('/user/create', methods=['POST'])
def user_create():
    #do the creating
    return redirect('/')


@app.route('/user/<int:id>')
def user_show(id):
    return render_template("user_show".html)

@app.route('/user/<int:id>/edit')
def user_edit(id):
    return render_template("user_edit.html")

@app.route('/user/<int:id>/update', methods=['POST'])
def user_update(id):
    return redirect('/')

@app.route('/user/<int:id>/delete')
def user_delete(id):
    return redirect('/')

# '/user/new' -> display the route with the form
# '/user/create' -> process the form from above
# '/user/<int:id>' -> display the user's info -> Show
# '/user/<int:id>/edit' -> display the user's info in a form so that they can edit it
# '/user/<int:id>/update' -> process the edit form
# '/user/<int:id>/delete' -> delete the user at that id

```

## create  \_\_init__.py file
```PY
from flask import Flask
#app = instance of Flask(class)
app = Flask(__name__)
app.secret_key = "do not forget to add secret key"
```