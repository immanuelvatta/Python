# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    DB = 'first_flask'
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['update_at']
    
    # Now we use class methods to query our database
    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM friends;"
    #     # make sure to call the connectToMySQL function with the schema you are targeting.
    #     results = connectToMySQL('first_flask').query_db(query)
    #     # Create an empty list to append our instances of friends
    #     friends = []
    #     # Iterate over the db results and create instances of friends with cls.
    #     for friend in results:
    #         friends.append( cls(friend) )
    #     return friends
    
    # class method to save our friend to the database
    
    #CREATE
    @classmethod
    def save(cls, data ):
        query = """
                INSERT INTO friends ( first_name , last_name , occupation) 
                VALUES ( %(fname)s , %(lname)s , %(occ)s);
        """
        # data is a dictionary that will be passed into the save method from server.py
        results = connectToMySQL(cls.DB).query_db( query, data )
        return results
    
    #READ
    # the get_one method will be used when we need to retrieve just one specific row of the table
    @classmethod
    def get_one(cls, id):
        query = """SELECT * from friends
                WHERE id = %(id)s"""
        results = connectToMySQL(cls.DB).query_db(query,{"id: id"})
                    # to return an actual object we use cls() and pass the dictionary into it
        one_record = cls(results[0])
        return one_record
    
    # the get_all method will be used when we need to retrieve all the rows of the table 
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM friends;"""
        results = connectToMySQL(cls.DB).query_db(query)
        all_friends = []
        for row in results:
            #make object
            #add to list
            all_friends.append(cls(row))
        return all_friends