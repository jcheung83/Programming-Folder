from flask import Flask, render_template  # added render_template!
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/table/')
def generate_table():
    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'},
    {'first_name' : 'Mark', 'last_name' : 'McGuire'},
    {'first_name' : 'Barry', 'last_name' : 'Bonds'}
    ]
    return render_template("index.html", users=users)
if __name__=="__main__":
    app.run(debug=True)  