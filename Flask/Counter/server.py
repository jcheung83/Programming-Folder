from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
    if 'counter' in session:
        print('key exists!')
        session['counter'] += 1
        print(session['counter'])
    else:
        print("key 'counter' does NOT exist")
        session['fake_counter'] = 1
        session['counter'] = 1
        print(session['counter'])
    return render_template("index.html")

@app.route('/addtwo')
def countupbtn():
    print(f"Adding 2 to the fake counter, now at {session['counter']}")
    session['fake_counter'] += 2
    return redirect('/')

@app.route('/reset')
def clearbtn():
    print("Resetting fake counter to 1")
    session['fake_counter'] = 1
    return redirect('/')

@app.route('/add_fake', methods=['POST'])
def add_fake():
    number = int(request.form['addnumber'])
    session['fake_counter'] += number
    print(f"Adding {request.form['addnumber']} to the fake counter, how at {session['counter']}")
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return 'Visits deleted'
if __name__=="__main__":   
    app.run(debug=True)   

# @app.route('/users', methods=['POST'])
# def create_user():
#     print("Got Post Info")
#     print(request.form)
#     # Here we add two properties to session to store the name and email
#     session['username'] = request.form['name']
#     session['useremail'] = request.form['email']
#     return redirect('/show') 
    
# # adding this method
# @app.route('/show')
# def show_user():
#     return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])

