from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])         
def enter_data():
    print(request.form)
    print(f"Name {request.form['name']}, location {request.form['location']}, language {request.form['location']}, comment {request.form['comment']}")
    name = request.form['name'].strip()
    location = request.form['location'].strip()
    language = request.form['language'].strip()
    comment = request.form['comment'].strip()
    return render_template("output.html", name=name, location=location, language=language, comment=comment)

if __name__=="__main__":   
    app.run(debug=True)    