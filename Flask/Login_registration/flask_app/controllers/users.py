from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, which is made by invoking the function Bcrypt with our app as an argument
from flask_app.models.user import User

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/create', methods=['POST'])
def create():
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash,
        "birthday": request.form['birthday']
    }
    if not User.validate(request.form):
        return redirect('/')
    User.save(data)
    user_id = User.get_last()
    session['user_id'] = user_id[0]['ID']
    print(session['user_id'])
    return redirect('/success')

@app.route('/success')
def show():
    print(session['user_id'])
    data = {
        "id": session['user_id']
    }
    current_user = User.get_info_from_id(data)
    email = current_user[0]['email']
    return render_template("success.html", email=email)

@app.route('/delete/<id>')
def delete(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect('/')

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
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    print(session['user_id'])
    data = {
        "id": session['user_id']
    }
    current_user = User.get_info_from_id(data)
    return render_template("dashboard.html", current_user=current_user)

@app.route('/logout')
def logout():
    session.clear()
    print("session cleared")
    return redirect('/')