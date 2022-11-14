import re	# the regex module
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

# create a regular expression object that we'll use later   
class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.under30 = data['under30']
        # self.user_id = data['user_id']
        self.user = data['user']
        
    @classmethod
    def delete( cls, data ):
        query = "DELETE FROM recipes where ID = %(id)s;"
        return connectToMySQL('recipes').query_db(query, data)

    # class method to save our user to the database
    @classmethod
    def save( cls, data ):
        query = "INSERT INTO recipes ( name , description, instructions, date, under30, user_id ) VALUES ( %(name)s, %(description)s, %(instructions)s, %(date)s, %(under30)s, %(user.id)s );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('recipes').query_db(query, data)

    @staticmethod
    def validate( recipe ):
        is_valid = True
        if len(recipe['name']) < 3 or len(recipe['description']) < 3 or len(recipe['instructions']) < 3:
            flash("Each field must be at least 3 characters.")
            is_valid = False
        return is_valid

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('recipes').query_db(query)
        # Create an empty list to append our instances of users
        recipes = []
        # Iterate over the db results and create instances of users with cls.
        for one_recipe in results:
            recipes.append( cls(one_recipe) )
        return recipes

    @classmethod
    def get_info_from_id(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL('recipes').query_db(query, data)
        recipes = cls(results[0])   
        return recipes

    @classmethod
    def edit_recipe(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, under30 = %(under30)s, date = %(date)s WHERE id = %(id)s;"
        return connectToMySQL('recipes').query_db(query, data)

    @classmethod
    def get_name_with_recipes(cls):
        query = "SELECT recipes.id, recipes.name, recipes.description, recipes.instructions, recipes.date, recipes.under30, recipes.user_id, users.first_name FROM recipes INNER JOIN users ON recipes.user_id = users.id ORDER by recipes.id;"
        results = connectToMySQL('recipes').query_db(query)
        return results