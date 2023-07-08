from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "sshhhhhhh"

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/character/create', methods=['POST'])
def character_create():
    #create the character
    #store the character into session
    # session['name'] = request.form['name']
    session['data'] = {
        **request.form
    }
    #redirect to display route
    
    return redirect('/character')

#  ACtion(redirect) or Display()
@app.route('/character')
def character_show():
    if 'data' not in session:
        return redirect('/')
    
    return render_template('character_show.html')

@app.route('/character/reset')
def reset():
    session.clear()
    return redirect('/')
    

if __name__=="__main__":
    app.run(debug=True)
