from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.email import Email

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/create', methods=['POST'])
def create():
    data = {
        "name": request.form['name'],
    }
    if not Email.validate(request.form):
        return redirect('/')
    Email.save(data)
    return redirect('/success')

@app.route('/success')
def show():
    emails = Email.get_all()
    user_email = Email.get_last()
    print(user_email)
    return render_template("success.html", emails=emails, user_email=user_email)

@app.route('/delete/<id>')
def delete(id):
    data = {
        "id": id
    }
    Email.delete(data)
    return redirect('/success')