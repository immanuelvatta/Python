from flask_app import app

#import controllers
from flask_app.controllers import controller_user

if __name__=="__main__":
    app.run(debug=True)
