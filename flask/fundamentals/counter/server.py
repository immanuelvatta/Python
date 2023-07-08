from flask import Flask, render_template, request,redirect, session

app = Flask(__name__)
app.secret_key = "topsecretkey"

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 1
    else:
        session["count"] += 1
    return render_template('index.html')

@app.route('/count', methods=['POST'])
def counting_two():
    session['count'] += 1
    return redirect('/')

# @app.route('/input', methods=['POST'])
# def input():
    

#! Add a "/destroy_session" route that clears the session and redirects to the root route. Test it.
@app.route('/destroy_session', methods=['POST'])
def destroy():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
