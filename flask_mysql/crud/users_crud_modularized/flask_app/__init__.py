from flask import Flask

#init instance of flask
app = Flask(__name__)

#session key
app.secret_key = "shhhhhhhhhh"