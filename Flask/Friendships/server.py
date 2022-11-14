# server.py
from flask_app.controllers import friendship
from flask_app import app

if __name__ == "__main__":
    app.run(debug=True)