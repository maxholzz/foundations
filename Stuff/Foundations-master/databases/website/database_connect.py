## simple function for reading from a sqlite database and returning a list
# takes a single argument of the neighborhood name, and returns a list of 
# resturants in the neighborhood.

# import the python library for SQLite 
import sqlite3

def get_restaurants(neighborhood_input):

    # connect to the database file, and create a connection object
    db_connection = sqlite3.connect('restaurants.db')

    # create a database cursor object, which allows us to perform SQL on the database. 
    db_cursor = db_connection.cursor()

    # define a query, taking the string input for the neighborhood name 

    query = """SELECT * from restaurants
                INNER JOIN neighborhoods ON restaurants.NEIGHBORHOOD_ID=neighborhoods.ID
                WHERE neighborhoods.NAME="{neighborhood_placeholder}"
            """.format(neighborhood_placeholder=neighborhood_input)

    db_cursor.execute(query)

    # store the result in a local variable. 
    # this will be a list of tuples, where each tuple represents a row in the table
    list_restaurants = db_cursor.fetchall()

    db_connection.close()

    return(list_restaurants)
