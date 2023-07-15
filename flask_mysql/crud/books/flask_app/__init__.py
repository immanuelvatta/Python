from flask import Flask
#app = instance of Flask(class)
app = Flask(__name__)
app.secret_key = "do not forget to add secret key"
DATABASE = 'books_db'