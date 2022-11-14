from flask import Flask, render_template  # added render_template!
app = Flask(__name__)   
                  
@app.route('/')
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response     
@app.route('/play/')                           
def index():
    # Render 3 blue boxes
    return render_template("index.html", phrase="blue", times=3)	# notice the 2 new named arguments!
@app.route('/play/<number>')
def make_boxes(number):
    # Render x number of blue boxes
    if number.isnumeric():
        number = int(number)
        print(number)
        return render_template("index.html", phrase="blue", times=number)
    else:
        return "Error, not an int"
@app.route('/play/<number>/<color>')
def make_more_boxes(number, color):
    # Render x number of color boxes
    if number.isnumeric():
        number = int(number)
        print(number)
        return render_template("index.html", phrase=color, times=number)
    else:
        return "Error, not an int"
if __name__=="__main__":
    app.run(debug=True)        

