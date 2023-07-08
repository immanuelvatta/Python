from flask import Flask
# app = instance of Flask (class)
app = Flask(__name__)

#THIS WILL MOVE!!!
@app.route('/')
def hello_world():
    return 'Hello World! Hello Immanuel'

@app.route('/second_route')
def second_route():
    return "this is my 2nd route"

@app.route('/third_route/<name>')
def third_route(name):
    return f"Hi my name is {name}"

# end of moving content

# MAKE SURE THIS IS AT THE BOTTOM
if __name__=="__main__":
    app.run(debug=True)

