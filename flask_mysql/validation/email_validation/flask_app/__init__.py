from flask import Flask
#app = instance of Flask(class)
app = Flask(__name__)
app.secret_key = "immanuel's secret key"
DATABASE = "email_db"