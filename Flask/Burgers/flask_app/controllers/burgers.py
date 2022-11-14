# burgers.py
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.burger import Burger

@app.route('/')
def index():
	return "Welcome!"
	
# gets all the burgers and returns them in a list of burger objects .
@app.route('/burgers')
def burgers():
	return render_template('results.html',burgers=Burger.get_all())

# gets all the burgers and returns them in a list of burger objects .
@app.route('/create/burger',methods=['POST'])
def create_burger():
	data = {
        	"name" : request.form['name'],
        	"bun" : request.form['bun'],
        	"meat" : request.form['meat'],
        	"calories" : request.form['calories']
	}
	if not Burger.validate_burger(data):
        # redirect to the route where the burger form is rendered.
    	return redirect('/')
    # else no errors:
    Burger.save(request.form)
    return redirect("/burgers")
        