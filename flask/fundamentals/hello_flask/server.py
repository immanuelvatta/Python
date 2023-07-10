from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    # return 'Hello World!'  # Return the string 'Hello World!' as a response
    return render_template("index.html")

@app.route('/success')
def success():
    return "Success!"


@app.route('/hello/<string:name>/<int:num>')
def hello(name, num):
    # return f"Hello {name * num}"
    return render_template("hello.html", name=name, num=num)

@app.route('/users/<username>/<id>') # for a route '/users/____/___', two parameters in the url get passed as username and id
def show_user_profile(username,id):
    print(username)
    print(id)
    return f"username: {username}, id: {id}"

# Here the second parameter is cast into an integer before being passed to the function
@app.route('/helloa/<name>/<int:num>')
def helloa(name,num):
    return f"Hello, {name * num} "



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)
    # app.run(debug=True, host="localhost", port=8000)    # Run the app in debug mode.