import sqlite3

# connect to the database file, and create a connection object
db_connection = sqlite3.connect('restaurants.db')

# create a database cursor object, which allows us to perform SQL on the database. 
db_cursor = db_connection.cursor()

# run a first query 
#db_cursor.execute("SELECT * from restaurants WHERE NEIGHBORHOOD_ID = '1'")
db_cursor.execute("INSERT INTO restaurants (NAME, NEIGHBORHOOD_ID, PRICE_RANGE_ID) VALUES ('Mmahh', 1, 1)")

# store the result in a local variable. 
# this will be a list of tuples, where each tuple represents a row in the table
db_connection.commit()

db_connection.close()