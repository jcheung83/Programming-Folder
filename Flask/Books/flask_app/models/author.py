import re	# the regex module
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def delete( cls, data ):
        query = "DELETE FROM authors where id = %(id)s;"
        return connectToMySQL('books').query_db(query, data)

    # class method to save our user to the database
    @classmethod
    def save( cls, data ):
        query = "INSERT INTO authors ( name , created_at, updated_at ) VALUES ( %(name)s, NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('books').query_db(query, data)

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('books').query_db(query)
        # Create an empty list to append our instances of users
        authors = []
        # Iterate over the db results and create instances of users with cls.
        for one_author in results:
            authors.append( cls(one_author) )
        return authors
        
    @classmethod
    def get_info_from_id(cls, data):
        query = "SELECT * FROM authors WHERE id = %(id)s;"
        results = connectToMySQL('books').query_db(query, data)
        print(results)
        info = cls(results[0])
        print(info)
        return info

    @classmethod
    def favorite_book(cls, data):
        query = "INSERT INTO favorites ( author_id, book_id ) SELECT %(author_id)s, %(book_id)s WHERE NOT EXISTS (SELECT author_id, book_id FROM favorites WHERE author_id = %(author_id)s AND book_id = %(book_id)s);"
        return connectToMySQL('books').query_db(query, data)

    @staticmethod
    def validate_favorite( info ):
        isValid = True
        query = "SELECT * from favorites;"
        results = connectToMySQL('books').query_db(query)
        for favorite in results:
            print("Favorite:",favorite, type(favorite))
            print("Info:",info, type(info))
            print(info.author_id)
            if (str(favorite.author_id) == str(info[0].author_id)) and (str(favorite.book_id == str(info[0].book_id))):
                flash("Favorite already exists")
                isValid = False
        return isValid    

    @classmethod
    def get_favorites(cls, data):
        query = "SELECT * FROM authors INNER JOIN favorites ON favorites.author_id = authors.id INNER JOIN books ON favorites.book_id = books.id WHERE books.id = %(id)s;"
        results = connectToMySQL('books').query_db(query, data)
        authors = []
        # Iterate over the db results and create instances of users with cls.
        for author in results:
            authors.append( cls(author) )
        return authors