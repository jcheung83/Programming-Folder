import re	# the regex module
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def delete( cls, data ):
        query = "DELETE FROM books where id = %(id)s;"
        return connectToMySQL('books').query_db(query, data)

    # class method to save our user to the database
    @classmethod
    def save( cls, data ):
        query = "INSERT INTO books ( title , num_of_pages, created_at, updated_at ) VALUES ( %(title)s, %(num_of_pages)s, NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('books').query_db(query, data)

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('books').query_db(query)
        # Create an empty list to append our instances of users
        books = []
        # Iterate over the db results and create instances of users with cls.
        for one_book in results:
            books.append( cls(one_book) )
        return books
        
    @classmethod
    def get_info_from_id(cls, data):
        query = "SELECT * FROM books WHERE id = %(id)s;"
        results = connectToMySQL('books').query_db(query, data)
        info = cls(results[0])
        return info

    @classmethod
    def get_favorites(cls, data):
        query = "SELECT * FROM books INNER JOIN favorites ON favorites.book_id = books.id INNER JOIN authors ON favorites.author_id = authors.id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books').query_db(query, data)
        books = []
        # Iterate over the db results and create instances of users with cls.
        for book in results:
            books.append( cls(book) )
        return books