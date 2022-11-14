# users.py
from flask_app import app
from flask import render_template,redirect,request,session,flash
# import the class from user.py
from flask_app.models.user import User

@app.route('/')         
def index():
    return render_template("index.html")
    
@app.route('/result', methods=['POST'])         
def enter_data():
    # print(request.form)
    data = {
        "name": request.form['name'],
        "location": request.form['location'],
        "language": request.form['language'],
        "comment": request.form['comment']
    }
    if not User.validate_user(request.form):
        return redirect('/')
    else:
        User.save(data)
    return render_template("output.html", data=data)