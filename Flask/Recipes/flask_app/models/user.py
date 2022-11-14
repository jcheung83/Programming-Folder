import re	# the regex module
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import recipe

# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def delete( cls, data ):
        query = "DELETE FROM users where ID = %(id)s;"
        return connectToMySQL('recipes').query_db(query, data)

    # class method to save our user to the database
    @classmethod
    def save( cls, data ):
        query = "INSERT INTO users ( first_name , last_name, email, password, created_at, updated_at ) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('recipes').query_db(query, data)

    @staticmethod
    def validate( user ):
        is_valid = True

        # test whether the email already exists in the database
        query = "SELECT email FROM users"
        results = connectToMySQL('recipes').query_db(query)
        for one_user in results:
            if user['email'] == str(one_user['email']):
                flash("Email address already exists, please choose another one.")
                print("already exists")
                is_valid = False

        if(not user['first_name'] or not user['last_name'] or not user['email'] or not user['password']):
            flash("All fields are required.")
            is_valid = False

        if len(user['first_name']) < 2 or len(user['last_name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False

        if user['password'] != user['password2']:
            flash("Password fields do not match.")
            is_valid = False

        # test whether the email matches the correct pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address! Please try again with a valid email address.")
            is_valid = False

        return is_valid

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('recipes').query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for one_user in results:
            users.append( cls(one_user) )
        return users

    @classmethod
    def get_last(cls):
        query = "SELECT ID FROM users ORDER BY ID DESC LIMIT 1;"
        results = connectToMySQL('recipes').query_db(query)
        users = cls(results[0])
        return users
        
    @classmethod
    def get_info_from_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('recipes').query_db(query, data)
        users = cls(results[0])
        return users

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('recipes').query_db(query, data)
        if len(results) < 1:
            return False
        users = cls(results[0])
        return users

    @classmethod
    def get_name_from_id(cls, data):
        query = "SELECT first_name FROM users WHERE id = %(user_id)s;"  
        results = connectToMySQL('recipes').query_db(query, data)
        users = cls(results[0])
        return users
        