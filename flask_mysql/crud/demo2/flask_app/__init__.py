from flask import Flask
#app = instance of Flask(class)
app = Flask(__name__)
app.secret_key = "do not forget to add secret key"

DATABASE = "july_car_dealer_2023_db"