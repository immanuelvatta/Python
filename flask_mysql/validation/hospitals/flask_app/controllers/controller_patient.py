from flask_app import app , bcrypt
from flask import render_template, redirect, session, request
from flask_app.models.model_patient import Patient



@app.route('/patient/create', methods=['POST'])
def patient_create():
    #do something so we redirect
    
    #clone the request dictionary 
    data = {**request.form}
    #Validate
    is_valid = Patient.validate(data)
    if is_valid == False:
        return redirect('/')
    # hash the password

    # create the patient
    data['hospital_id'] = session['hospital_id']
    Patient.create(data)
    
    return redirect('/dashboard')

@app.route('/patient/<int:id>')
def patient_show(id):
    if 'hospital_id' not in session:
        return redirect('/')
    
    patient = Patient.get_one({'id': id})
    
    return render_template('patient_show.html', patient = patient)

#display page -> render template
@app.route('/patient/<int:id>/edit')
def patient_edit(id):
    if 'hospital_id' not in session:
        return redirect('/')
    
    patient = Patient.get_one({'id': id})
    
    return render_template('patient_edit.html', patient = patient)

#action route -> redirect
@app.route('/patient/<int:id>/update', methods = ['POST'])
def patient_update(id):
    if 'hospital_id' not in session:
        return redirect('/')
    #validate
    data = {**request.form}
    #call redirect
    is_valid = Patient.validate(data)
    if not is_valid:
        return redirect(f'/patient/{id}/edit')
    data['id'] = id
    Patient.update_one(data)
    return redirect('/dashboard')

@app.route('/patient/<int:id>/delete')
def patient_delete(id):
    if 'hospital_id' not in session:
        # if id !=session['patient_id']:
            return redirect('/dashboard')
        
    Patient.delete_one({'id': id})
    return redirect('/patient/logout') 