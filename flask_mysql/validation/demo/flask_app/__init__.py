from flask import Flask, render_template, session, request, redirect
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.secret_key = "do not forget to add secret key"
bcrypt = Bcrypt(app)