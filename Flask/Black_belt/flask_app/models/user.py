import re	# the regex module
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import show

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

    # delete method for user
    @classmethod
    def delete( cls, data ):
        query = "DELETE FROM users where ID = %(id)s;"
        return connectToMySQL('tvshows').query_db(query, data)

    # class method to save our user to the database
    @classmethod
    def save( cls, data ):
        query = "INSERT INTO users ( first_name , last_name, email, password, created_at, updated_at ) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('tvshows').query_db(query, data)

    # validate user data, including matching passwords, and email pattern validation
    @staticmethod
    def validate( user ):
        is_valid = True

        # test whether the email already exists in the database
        query = "SELECT email FROM users"
        results = connectToMySQL('tvshows').query_db(query)
        for one_user in results:
            if user['email'] == str(one_user['email']):
                flash("Email address already exists, please choose another one.")
                print("already exists")
                is_valid = False

        # ensure all fields are filled out
        if(not user['first_name'] or not user['last_name'] or not user['email'] or not user['password']):
            flash("All fields are required.")
            is_valid = False

        # names must be at least 2 char
        if len(user['first_name']) < 2 or len(user['last_name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False

        # password fields must match
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
        results = connectToMySQL('tvshows').query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for one_user in results:
            users.append( cls(one_user) )
        return users

    # get last id from db, needed to get session id after user creates account
    @classmethod
    def get_last(cls):
        query = "SELECT id FROM users ORDER BY id DESC LIMIT 1;"
        results = connectToMySQL('tvshows').query_db(query)
        return results
        
    # get all info about a specific user
    @classmethod
    def get_info_from_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('tvshows').query_db(query, data)
        info = cls(results[0])
        return info

    # get all info about user from email, needed to check if email already exists in db
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('tvshows').query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    # return ids of shows that the user likes
    @classmethod
    def get_likes(cls, data):
        query = "SELECT likes.show_id FROM likes where user_id = %(id)s;"
        results = connectToMySQL('tvshows').query_db(query, data)
        print(results)
        return results

    # insert into db that a user likes a show
    @classmethod
    def like_show(cls, data):
        query = "INSERT INTO likes ( user_id, show_id ) SELECT %(user_id)s, %(show_id)s WHERE NOT EXISTS (SELECT user_id, show_id FROM likes WHERE user_id = %(user_id)s AND show_id = %(show_id)s);"
        return connectToMySQL('tvshows').query_db(query, data)

    # insert into db that a user likes a show
    @classmethod
    def unlike_show(cls, data):
        query = "DELETE FROM likes WHERE user_id = %(user_id)s AND show_id = %(show_id)s;"
        return connectToMySQL('tvshows').query_db(query, data)