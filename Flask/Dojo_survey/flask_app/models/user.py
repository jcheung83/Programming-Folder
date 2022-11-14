# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# model the class after the user table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # class method to save our user to the database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( name , location , language, comment, created_at, updated_at ) VALUES ( %(name)s , %(location)s , %(language)s , %(comment)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojosurvey').query_db(query, data)

    # class method to delete our user to the database
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('dojosurvey').query_db(query, data)
    
    # class method to pull our user data from the database, given the id
    @classmethod
    def get_data(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        return connectToMySQL('dojosurvey').query_db(query, data)

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojosurvey').query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append( cls(user) )
        return users

    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true
        if len(user['name']) < 3:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if len(user['comment']) < 30:
            flash("Comment is required and must be at least 30 characters long.")
            is_valid = False
        return is_valid