from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response        
@app.route('/dojo')     # import statements, maybe some other routes
def success():
    return "Dojo!"
@app.route('/say/<name>') # for a route '/say/____' anything after '/say/' gets passed as a variable 'name'
def hello(name):
    if isinstance(name, str):
        return "Hi " + name + "!"
    else:
        return "Error, not a string"
@app.route('/repeat/<times>/<word>') #for a route '/repeat/____/____', repeat the word times number of times
def speak(times, word):
    print(type(word))
    output=""
    if isinstance(word, str):
        if times.isnumeric():
            times = int(times)
            for x in range(times):
                output += word
                output += '\n'
            return output
        else:
            return "Error, not an int"
    else:
        return "Error, not a string"  
@app.errorhandler(404)
def page_not_found(error):
    return "The page you are looking for does not exist"
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.