import random
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "topsecret"

@app.route('/')
def index():
    if 'num' not in session:
        session['num'] = random.randint(1,100) # random number between 1-100
    print(session['num'])
    return render_template('index.html')

@app.route('/guess',methods=['POST'])
def guess():
    session['guess']  = int(request.form['guess'])
    return redirect('/')

#!route that clears the session and redirects to the root route
@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
