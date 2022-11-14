from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo
# ninja.py

class Ninja:
    def __init__(self,db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.age = db_data['age']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
    
    # class method to save our ninja to the database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas ( first_name , last_name , age , dojo_id, created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(age)s , %(dojo_id)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos').query_db(query, data)

    # class method to delete our ninja to the database
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL('dojos').query_db(query, data)

    # class method to pull our ninja data from the database, given the id
    @classmethod
    def get_data(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL('dojos').query_db(query, data)