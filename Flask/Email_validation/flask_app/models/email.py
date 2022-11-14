import re	# the regex module
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class Email:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def delete( cls, data ):
        query = "DELETE FROM emails where ID = %(id)s;"
        return connectToMySQL('email').query_db(query, data)

    # class method to save our user to the database
    @classmethod
    def save( cls, data ):
        query = "INSERT INTO emails ( name , created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('email').query_db(query, data)

    @staticmethod
    def validate( email ):
        is_valid = True

        # test whether the email already exists in the database
        query = "SELECT name FROM emails"
        results = connectToMySQL('email').query_db(query)
        for name in results:
            print (email['name'],"==",name)
            if email['name'] == str(name['name']):
                flash("Email address already exists, please choose another one")
                print("already exists")
                is_valid = False

        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(email['name']): 
            flash("Invalid email address! Please try again with a valid email address")
            is_valid = False
        return is_valid

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('email').query_db(query)
        # Create an empty list to append our instances of users
        emails = []
        # Iterate over the db results and create instances of users with cls.
        for email in results:
            emails.append( cls(email) )
        return emails

    @classmethod
    def get_last(cls):
        query = "SELECT * FROM emails ORDER BY ID DESC LIMIT 1;"
        results = connectToMySQL('email').query_db(query)
        return results