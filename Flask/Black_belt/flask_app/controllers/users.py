from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, which is made by invoking the function Bcrypt with our app as an argument
from flask_app.models.user import User
from flask_app.models.show import Show

@app.route('/')         
def index():
    return render_template("index.html")

# login page
@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { 
        "email" : request.form["email"] 
    }
    user_in_db = User.get_by_email(data)
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
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
    return redirect('/shows')

# create a new user, redirects to dashboard if successful
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
    session['user_id'] = user_id[0]['id']
    print(session['user_id'])
    return redirect('/shows')

# dashboard page for all shows
@app.route('/shows')
def all_shows():
    if 'user_id' not in session:
        return redirect('/')
    print("User id:",session['user_id'])
    data = {
        "id": session['user_id']
    }
    id=session['user_id']
    current_user = User.get_info_from_id(data)
    first_name = current_user.first_name
    shows = Show.get_all()
    likes = User.get_likes(data)
    dict={}
    for i in range (len(likes)):
        dict[likes[i]['show_id']] = 1    
    return render_template("dashboard.html", first_name=first_name, id=id, shows=shows, dict=dict)

# create a new show
@app.route('/shows/new')
def new_show():
    if 'user_id' not in session:
        return redirect('/')
    print(session['user_id'])
    return render_template("new.html")

# redirects to dashboard if successful, returns to new show page if not
@app.route('/create_show', methods=['POST'])
def create_show():
    if 'user_id' not in session:
        return redirect('/')
    print(session['user_id'])
    data = {
        "title": request.form['title'],
        "network": request.form['network'],
        "date": request.form['date'],
        "description": request.form['description'],
        "user_id": session['user_id']
    }
    if not Show.validate(request.form):
        return redirect('/shows/new')
    Show.save(data)
    return redirect('/shows')

# show the tv show data
@app.route('/shows/<id>')
def show_tvshow(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": id
    }
    show = Show.get_info_from_id(data)
    likes = Show.count_likes(data)
    data = {
        "id": show.user_id
    }
    poster_info = User.get_info_from_id(data)
    return render_template("show.html", show=show, poster_info=poster_info, likes=likes)

# delete a show only if the user created it
@app.route('/delete/shows/<id>')
def delete_show(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": id
    }
    show = Show.get_info_from_id(data)
    print(show.user_id)
    if show.user_id != session['user_id']:
        flash("You cannot edit or delete shows that you did not create!")
        return redirect('/shows')
    Show.delete_likes(data)
    Show.delete(data)
    return redirect('/shows')

# edit a show only if a user created it
@app.route('/shows/edit/<id>')
def edit_show(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": id
    }
    show = Show.get_info_from_id(data)
    if show.user_id != session['user_id']:
        flash("You cannot edit or delete shows that you did not create!")
        return redirect('/shows')
    return render_template("edit.html", show=show)

# edit route for show
@app.route('/edit', methods=["POST"])
def edit():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": request.form['id'],
        "title": request.form['title'],
        "network": request.form['network'],
        "date": request.form['date'],
        "description": request.form['description']
    }
    id = request.form['id']
    if not Show.validate(request.form):
        return redirect(f"/shows/edit/{id}")
    Show.edit_show(data)
    return redirect('/shows')

# logout, clear session
@app.route('/logout')
def logout():
    session.clear()
    print("session cleared")
    return redirect('/')

# likes a show
@app.route('/like/<user_id>/<show_id>')
def like(user_id, show_id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "user_id": user_id,
        "show_id": show_id
    }
    User.like_show(data)
    return redirect('/shows')

#unlikes a show
@app.route('/unlike/<user_id>/<show_id>')
def unlike(user_id, show_id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "user_id": user_id,
        "show_id": show_id
    }
    User.unlike_show(data)
    return redirect('/shows')