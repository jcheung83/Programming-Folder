from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'e3kfdm2e04kmfl4fll1' # set a secret key for security purposes

@app.route('/')
def index():
    session['count'] = 0
    if 'high_score_count' not in session:
        session['high_score_count'] = 0
        session['high_score_names'] = []
        session['high_scores'] = []
    if 'number' in session:
        print(f"The number exists, it is: {session['number']}")
    else:
        print("The number does NOT exist")
        session['number'] = random.randint(1,100)
        print(f"The number is now set to: {session['number']}")
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def evaluate():
    guess = int(request.form['guessnumber'])
    session['count'] += 1
    if (session['count'] == 5 and guess != session['number']):
        print("user lost")
        return render_template("fail.html")
    else: 
        if guess < session['number']: 
            print("too low")
            count=session['count']
            return render_template("miss.html", message="Too low", color="red", count=count)
        elif guess > session['number']:
            print("too high")
            count=session['count']
            return render_template("miss.html", message="Too high", color="red", count=count)
        elif guess == session['number']:
            print("yes!")
            count=session['count']
            message = str(session['number']) + " was the number!"
            return render_template("success.html", message=message, color="green", count=count)

@app.route('/reset')
def clearbtn():
    print("Resetting number")
    session['number'] = random.randint(1,100)
    session['count'] = 0
    return redirect('/')

@app.route('/highscore', methods=['POST'])
def scoreboard():
    print(f"number of high scores: {session['high_score_count']}")
    session['high_score_names'].append(request.form['high_score_name'])
    session['high_scores'].append(session['count'])
    high_score_names = session['high_score_names']
    high_scores = session['high_scores']
    session['number'] = random.randint(1,100)
    return render_template("high_score.html", high_score_names=high_score_names, high_scores=high_scores)

@app.route('/resetall')
def clearall():
    session.clear()
    print("Clearing session")
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)   