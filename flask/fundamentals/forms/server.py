from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "secret key"

#display route
@app.route('/')
def hello_world():
    session['name'] = 'immanuel'
    return render_template('index.html')

#action route (redirect route)
#TODO create route for users
@app.route('/users', methods=['POST'])
def users():
    print(request.form)
    copy_of_form = {
        # 'name': request.form['name'],
        # 'card_num': request.form['card_num']
        
        #* this will do what was done above
        **request.form
    }
    session['name'] = request.form['name']
    print("this is in user route")
    print(session['name'])
    # copy_of_form['name'] = 'joe'
    # print(copy_of_form)
    print("Charging your card now")
    return redirect('/success')

#display route
@app.route('/success')
def success():
    
    if 'name' not in session:
        return redirect('/')
    
    print("this is in the /success page")
    print(session['name'])
    print("*"*80)
    # print(request.form)
    print("*"*80)
    return render_template("success.html",tracking_num = 234234)




#Make SURE THIS IS AT THE BOTTOM
if __name__=="__main__":
    app.run(debug=True)