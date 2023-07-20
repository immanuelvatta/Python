from flask_app import app
from flask import render_template, redirect, session
from flask_app.models.model_hospital import Hospital

@app.route('/')
def index():
    if 'hospital_id' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'hospital_id' not in session:
        return redirect('/')
    
    hospital = Hospital.get_one({'id': session['hospital_id']})
    return render_template('dashboard.html' , hospital = hospital)