from flask_app import app
from flask_app.controllers import controller_author, controller_book
#TODO import controllers

#MAKE SURE THIS IS AT THE BOTTOM
if __name__=="__main__":
    app.run(debug=True)