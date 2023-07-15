from flask import render_template,request, redirect, session
from flask_app import app
from flask_app.models.model_survey import Survey


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form/create', methods=['POST'])
def form_create():
    if Survey.is_valid_survey(request.form):
        Survey.create(request.form)
        return redirect('/result')
    return redirect('/')

@app.route('/result')
def show_result():
    show_survey = Survey.get_one()
    # if 'data' not in session:
    #     return redirect('/')
    return render_template('result.html', show_survey = show_survey)

@app.route('/result/reset')
def reset():
    #! session.clear() removes everything
    # session.clear()
    # use del specific
    # del session['data']
    return redirect('/')