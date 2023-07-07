# Pre-checklist install
installing pipenv on a global scope


`!Only needs to be done once!`

```
pip install pipenv
``` 

# Start of checklist
- Create a folder for our new assignment
- go into that folder
- create the virtual env with flask

    ```
    pipenv install flask
    ```
- WARNING! Make sure pipfile & pipfile.lock are there!! If not FIX THIS NOW!!!
- activate virtual env
    ```
    pipenv shell
    ```
- Create server.py

    ```
    from flask import Flask  # Import Flask to allow us to create our app
    app = Flask(__name__)    # Create a new instance of the Flask class called "app"
    @app.route('/')          # The "@" decorator associates this route with the function immediately following
    def hello_world():
        return 'Hello World!'  # Return the string 'Hello World!' as a response
    if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
        app.run(debug=True)    # Run the app in debug mode.

    ```