from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']

        self.name = data['name']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    # gets all dojos
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo))
        return dojos

    # saves dojo info
    @classmethod
    def save_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return result

    # gets a single dojo with all attached ninjas
    @classmethod
    def get_one_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        # creating a single instance of dojo from query data
        one_dojo =  cls(result[0])
        # 
        for row in result:
            ninja_data = {
                'id' : row['ninjas.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'age' : row['age'],
                'created_at' : row['ninjas.created_at'],
                'updated_at' : row['ninjas.updated_at']
            }
            one_dojo.ninjas.append( ninja.Ninja( ninja_data ))
        return one_dojo
