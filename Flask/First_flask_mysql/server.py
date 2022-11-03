from flask import Flask, redirect, request, render_template
# import the class from user.py
from user import User
app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome. Go to /users to start."

@app.route('/users')
def show_users():
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users = users)
            
@app.route('/new')
def add():
    return render_template("add.html")

@app.route('/edit', methods=["POST"])
def edit():
    data = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email'],
        "id": request.form['id']
    }
    User.edit(data)
    return redirect('/users')

@app.route('/users/<id>/')
def show_one_user(id):
    data = {
        "id": id
    }
    user = User.get_data(data)
    return render_template("user.html", user_info=user)

@app.route('/users/<id>/edit')
def make_edits(id):
    data = {
        "id": id
    }
    user = User.get_data(data)
    return render_template("edit.html", user=user)

@app.route('/users/<id>/destroy')
def destroy(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect('/users')
        
@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email']
    }
    # We pass the data dictionary into the save method from the user class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)