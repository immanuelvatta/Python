# Pre-checklist install
installing pipenv on a global scope


`!Only needs to be done once!`

```console
pip install pipenv
``` 

# Start of checklist
- Create a folder for our new assignment
- go into that folder
- create the virtual env with flask

    ```console
    pipenv install flask
    ```
- WARNING! Make sure pipfile & pipfile.lock are there!! If not FIX THIS NOW!!!
- activate virtual env
    ```console
    pipenv shell
    ```
- Create server.py

    ```Py
    from flask import Flask, render_template, session, request, redirect

    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return render_template('index.html')


    if __name__=="__main__":
        app.run(debug=True)

    ```
-- Create templates folder
-- add index.html in templates folder
-- Test it out