import re	# the regex module
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

# create a regular expression object that we'll use later   
class Show:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.network = data['network']
        self.date = data['date']
        self.user_id = data['user_id']
        
    # delete the actual show
    @classmethod
    def delete( cls, data ):
        query = "DELETE FROM shows where id = %(id)s;"
        return connectToMySQL('tvshows').query_db(query, data)

    # delete the likes of the show first, to prevent foreign_key constraints
    @classmethod
    def delete_likes (cls, data):
        query = "DELETE FROM likes where show_id = %(id)s;"
        return connectToMySQL('tvshows').query_db(query, data)

    # class method to save our show to the database
    @classmethod
    def save( cls, data ):
        query = "INSERT INTO shows ( title, network, date, description, user_id ) VALUES ( %(title)s, %(network)s, %(date)s, %(description)s, %(user_id)s );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('tvshows').query_db(query, data)

    # ensure the info exists and is at least 3 char long
    @staticmethod
    def validate( show ):
        is_valid = True
        if(not show['title'] or not show['description'] or not show['network'] or not show['date']):
            flash("All fields are required.")
            is_valid = False

        if len(show['title']) < 3 or len(show['description']) < 3 or len(show['network']) < 3:
            flash("Each field must be at least 3 characters.")
            is_valid = False
        return is_valid

    # now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM shows;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('tvshows').query_db(query)
        # Create an empty list to append our instances of users
        shows = []
        # Iterate over the db results and create instances of users with cls.
        for one_show in results:
            shows.append( cls(one_show) )
        return shows

    # get all info about a specific show
    @classmethod
    def get_info_from_id(cls, data):
        query = "SELECT * FROM shows WHERE id = %(id)s;"
        results = connectToMySQL('tvshows').query_db(query, data)
        show = cls(results[0])
        return show

    # edit method for a show
    @classmethod
    def edit_show(cls, data):
        query = "UPDATE shows SET title = %(title)s, network = %(network)s, date = %(date)s, description = %(description)s WHERE id = %(id)s;"
        return connectToMySQL('tvshows').query_db(query, data)
    
    # count number of users who have liked the show
    @classmethod
    def count_likes(cls, data):
        query = "SELECT COUNT(likes.user_id) FROM likes INNER JOIN shows ON shows.id = likes.show_id WHERE shows.id = %(id)s;"
        results = connectToMySQL('tvshows').query_db(query, data)
        return results[0]['COUNT(likes.user_id)']

        
        