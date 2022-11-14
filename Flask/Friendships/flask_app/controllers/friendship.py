from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { 
        "email" : request.form["email"] 
    }
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect('/recipes')

@app.route('/create', methods=['POST'])
def create():
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash
    }
    if not User.validate(request.form):
        return redirect('/')
    User.save(data)
    user_id = User.get_last()
    session['user_id'] = user_id.id
    print(session['user_id'])
    return redirect('/recipes')

@app.route('/recipes')
def show():
    print(session['user_id'])
    data = {
        "id": session['user_id']
    }
    id=session['user_id']
    current_user = User.get_info_from_id(data)
    first_name = current_user.first_name
    recipes = Recipe.get_name_with_recipes()
    return render_template("dashboard.html", first_name=first_name, id=id, recipes=recipes)

@app.route('/recipes/new')
def dashboard():
    print(session['user_id'])
    return render_template("new.html")

@app.route('/create_recipe', methods=['POST'])
def create_recipe():
    print(session['user_id'])
    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "date": request.form['date'],
        "under30": request.form['under30'],
        "user_id": session['user_id']
    }
    if not Recipe.validate(request.form):
        return redirect('/recipes/new')
    Recipe.save(data)
    return redirect('/recipes')

@app.route('/recipes/<id>')
def show_recipe(id):
    data = {
        "id": id
    }
    recipe = Recipe.get_info_from_id(data)

    data = {
        "id": session['user_id']
    }
    current_user = User.get_info_from_id(data)
    first_name = current_user.first_name

    print(recipe.user_id)

    data = {
        "id": recipe.user_id
    }
    name = User.get_name_from_id(data)
    recipe_fname = name[0]

    return render_template("recipe.html", recipe=recipe, first_name=first_name, name=recipe_fname)

@app.route('/delete/recipes/<id>')
def delete_recipe(id):
    data = {
        "id": id
    }
    recipe = Recipe.get_info_from_id(data)
    print(recipe.user_id)
    if recipe.user_id != session['user_id']:
        flash("You cannot edit or delete recipes that you did not create!")
        return redirect('/recipes')
    Recipe.delete(data)
    return redirect('/recipes')

@app.route('/recipes/edit/<id>')
def edit_recipe(id):
    data = {
        "id": id
    }
    recipe = Recipe.get_info_from_id(data)
    print(recipe.user_id)
    if recipe.user_id != session['user_id']:
        flash("You cannot edit or delete recipes that you did not create!")
        return redirect('/recipes')
    return render_template("edit.html", recipe=recipe)

@app.route('/edit', methods=["POST"])
def edit():
    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "under30": request.form['under30'],
        "date": request.form['date'],
        "id": request.form['id']
    }
    id = request.form['id']
    if not Recipe.validate(request.form):
        return redirect(f"/recipes/edit/{id}")
    Recipe.edit_recipe(data)
    return redirect('/recipes')

@app.route('/logout')
def logout():
    session.clear()
    print("session cleared")
    return redirect('/')