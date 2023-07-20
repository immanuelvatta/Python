from flask_app import app , bcrypt
from flask import render_template, redirect, session, request
from flask_app.models.model_hospital import Hospital


@app.route('/hospital/login', methods=['POST'])
def hospital_login():
    #copy request.form
    data = {**request.form}
    #validate the form
    Hospital.validate_login(data)
    return redirect('/dashboard')

@app.route('/hospital/logout')
def hospital_logout():
    del session['hospital_id']
    return redirect('/')

@app.route('/hospital/create', methods=['POST'])
def hospital_create():
    #do something so we redirect
    
    #clone the request dictionary 
    data = {**request.form}
    #Validate
    is_valid = Hospital.validate(data)
    if is_valid == False:
        return redirect('/')
    # hash the password
    hash_pw = bcrypt.generate_password_hash(data['password'])
    #update the password in the data dictionary
    data ['password'] = hash_pw
    # create the hospital
    id = Hospital.create(data)
    session['hospital_id'] = id
    
    return redirect('/dashboard')

#display page -> render template
@app.route('/hospital/<int:id>/edit')
def hospital_edit(id):
    if 'hospital_id' not in session:
        return redirect('/')
    
    hospital = Hospital.get_one({'id': session ['hospital_id']})
    
    return render_template('hospital_edit.html', hospital = hospital)

#action route -> redirect
@app.route('/hospital/<int:id>/update', methods = ['POST'])
def hospital_update(id):
    if 'hospital_id' not in session:
        return redirect('/')
    #validate
    data = {**request.form}
    #call redirect
    is_valid = Hospital.validate_update(data)
    if not is_valid:
        return redirect(f'/hospital/{id}/edit')
    data['id'] = id
    Hospital.update_one(data)
    return redirect('/dashboard')

@app.route('/hospital/<int:id>/delete')
def hospital_delete(id):
    if 'hospital_id' not in session:
        # if id !=session['hospital_id']:
            return redirect('/dashboard')
        
    Hospital.delete_one({'id': id})
    return redirect('/hospital/logout') 