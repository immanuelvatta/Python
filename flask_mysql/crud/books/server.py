from flask_app import app

#TODO import controllers
from flask_app.controllers import controller_book, controller_author, controller_routes

#MAKE SURE THIS IS AT THE BOTTOM
if __name__=="__main__":
    app.run(debug=True)