from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL(DB).query_db(query)

        list_of_dojos = []
        for dojo in results:
            list_of_dojos.append(cls(dojo))
        return list_of_dojos

    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM dojos WHERE id = %(id)s;'
        result = connectToMySQL(DB).query_db(query, data)

        return cls(result[0])

    @classmethod
    def create_one(cls, data):
        query = 'INSERT INTO dojos (name) VALUES (%(name)s);'
        return connectToMySQL(DB).query_db(query, data)




