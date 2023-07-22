from flask_app import app, bcrypt

from flask import render_template, redirect, request, session
from flask_app.models.model_recipes import Recipe
from flask_app.models.model_user import User
#flip create and new in routes and def
#/recipe/new
@app.route('/recipe/new')
def recipe_new():
    if not session:
        return redirect('/')
    user = User.get_one(session['email'])
    
    return render_template("create_recipe.html", user = user)
#/recipe/create
@app.route('/recipe/create', methods = ["POST"])
def recipe_create():
    # if not session:
    #     return redirect('/')
    data = {
        **request.form
    }
    if not Recipe.recipe_validator(data):
        return redirect('/recipe/create')
    Recipe.create(data)
    return redirect('/user/success')


@app.route('/recipe/view/<int:id>')
def recipe_view(id):
    if not session:
        return redirect('/')
    user = User.get_one(session['email'])
    
    recipe  = Recipe.get_one_recipe(id)
    
    return render_template("display_recipe.html", user = user, recipe = recipe)


@app.route('/recipe/edit/<int:id>')
def recipe_edit(id):
    if not session:
        return redirect('/')
    user = User.get_one(session['email'])
    recipe = Recipe.get_one(id)
    return render_template("edit_recipe.html", recipe = recipe, user= user)


@app.route('/recipe/updated/<int:id>', methods = ['POST'])
def recipe_updated(id):
    data = {** request.form,
            'id' : id
            }
    if not Recipe.recipe_validator(data):
        return redirect(f'/recipe/edit/{id}')
    Recipe.update(data)
    return redirect('/user/success')

@app.route('/recipe/delete/<int:id>')
def recipe_delete(id):
    if not session:
        return redirect('/')
    Recipe.delete(id)
    return redirect('/user/success')
