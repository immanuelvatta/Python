from flask import Flask # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

#TODO localhost:5000/ - have it say "Hello World!"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

#TODO localhost:5000/dojo - have it say "Dojo!"
@app.route('/dojo')
def dojo():
    return "Dojo!"
'''
#TODO Create one url pattern and function that can handle the following examples:
localhost:5000/say/flask - have it say "Hi Flask!"
localhost:5000/say/michael - have it say "Hi Michael!"
localhost:5000/say/john - have it say "Hi John!" 
'''
@app.route('/say/<string:name>')
def print_name(name):
    return f"Hi {name.capitalize()}!"

'''
#TODO Create one url pattern and function that can handle the following examples 
# (HINT: path variables are by default passed as strings. How might you handle a number?):
localhost:5000/repeat/35/hello - have it say "hello" 35 times
localhost:5000/repeat/80/bye - have it say "bye" 80 times
localhost:5000/repeat/99/dogs - have it say "dogs" 99 times
'''
@app.route('/repeat/<int:num>/<string:words>')
def patterns(num,words):
    return f" {num * words } "

'''
Ensure that if the user types in any route other than the ones specified, 
they receive an error message saying "Sorry! No response. Try again."
'''
@app.errorhandler(404)
def handle_bad_request(e):
    return "Sorry! No response. Try again.",404
    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.