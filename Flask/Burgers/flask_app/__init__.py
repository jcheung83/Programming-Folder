# __init__.py
from flask import Flask
from flask import session
app = Flask(__name__)
app.secret_key = "waaaaaah"