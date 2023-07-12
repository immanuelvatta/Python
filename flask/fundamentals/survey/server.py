from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "sshhhhhhh"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form/create', methods=['POST'])
def form_create():
    session['data'] = {
        **request.form
    }
    return redirect('/result')

@app.route('/result')
def show_result():
    if 'data' not in session:
        return redirect('/')
    return render_template('result.html')

@app.route('/result/reset')
def reset():
    #! session.clear() removes everything
    # session.clear()
    # use del specific
    del session['data']
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)