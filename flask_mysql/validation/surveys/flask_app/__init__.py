from flask import Flask, session

app = Flask(__name__)

app.secret_key = "ssshssssh"

DATABASE = 'survey_db'