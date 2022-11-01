from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    fruit_total = int(request.form["apple"]) + int(request.form["blackberry"]) + int(request.form["raspberry"]) + int(request.form["strawberry"])
    print(f"Charging {request.form['first_name']} {request.form['last_name']} for {fruit_total} fruit")
    first_name = request.form['first_name'].strip()
    last_name = request.form['last_name'].strip()
    stud_id = request.form['student_id'].strip()
    apple = request.form['apple'].strip()
    blackberry = request.form['blackberry'].strip()
    raspberry = request.form['raspberry'].strip()
    strawberry = request.form['strawberry'].strip()
    return render_template("checkout.html", fname = first_name, lname = last_name, s_id = stud_id, a = apple, b = blackberry, r = raspberry, s = strawberry)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    