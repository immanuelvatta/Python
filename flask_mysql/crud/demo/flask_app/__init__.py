from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)

app.secret_key = "do not forget to add secret key"