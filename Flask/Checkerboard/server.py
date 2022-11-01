from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                
@app.route('/')
def hello_world():
    return render_template("index.html", x_times=8, y_times=8)
@app.route('/<x>')
def make_checkerboard(x):
    # the checkerboard
    if (x.isnumeric()):
        x = int(x)
        return render_template("index.html", x_times=x, y_times=8)
    else:
        return "Error, not an int"    
@app.route('/<x>/<y>')
def make_bigger_checkerboard(x, y):
    # the checkerboard
    if ((x.isnumeric()) and (y.isnumeric())):
        x = int(x)
        y = int(y)
        return render_template("index.html", x_times=x, y_times=y)
    else:
        return "Error, one of the numbers not an int"
@app.route('/<x>/<y>/<color1>/<color2>')
def make_different_checkerboard(x, y, color1, color2):
    # the checkerboard
    if ((x.isnumeric()) and (y.isnumeric())):
        x = int(x)
        y = int(y)
        return render_template("index.html", x_times=x, y_times=y, c1=color1, c2=color2)
    else:
        return "Error, one of the numbers not an int"
if __name__=="__main__":
    app.run(debug=True)        




