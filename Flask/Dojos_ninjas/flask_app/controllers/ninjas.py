from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
	return "Welcome!"

@app.route('/dojos')
def show_dojos():
    # call the get all classmethod to get all users
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("index.html", all_dojos = dojos)

@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    data = {
        "name": request.form['name']
    }
    Dojo.save(data)
    return redirect('/dojos')
    
@app.route('/ninjas')
def add_ninjas():
    dojos = Dojo.get_all()
    return render_template("add.html", dojos=dojos)

@app.route('/add', methods=["POST"])
def add():
    data = {
        "dojo_id": request.form['dojo_id'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age']
    }
    Ninja.save(data)
    return redirect('/dojos')

@app.route('/dojos/<id>')
def show_ninjas(id):
    data = {
        "dojo_id": id,
    }
    dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template("ninja.html", dojo=dojo)