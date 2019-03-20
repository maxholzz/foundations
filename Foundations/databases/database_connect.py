## simple demo script for showing how to connect to an sqlite DB 
# from Python, and run a simple SQL query 

# import the python library for SQLite 
import sqlite3

# connect to the database file, and create a connection object
db_connection = sqlite3.connect('restaurants.db')

# create a database cursor object, which allows us to perform SQL on the database. 
db_cursor = db_connection.cursor()

# run a first query 
db_cursor.execute("SELECT * FROM restaurants")
# store the result in a local variable. 
# this will be a list of tuples, where each tuple represents a row in the table
list_restaurants = db_cursor.fetchall()

print("list_restaurants contents:")
print(list_restaurants)


# create a database cursor object, which allows us to perform SQL on the database. 
db_cursor = db_connection.cursor()

# run a first query 
db_cursor.execute("SELECT * FROM restaurants WHERE NEIGHBORHOOD_ID = '1'")

# store the result in a local variable. 
# this will be a list of tuples, where each tuple represents a row in the table
list_restaurants = db_cursor.fetchall()

db_connection.close()

db_connection = sqlite3.connect('restaurants.db')

# create a database cursor object, which allows us to perform SQL on the database. 
db_cursor = db_connection.cursor()

# run a first query 
db_cursor.execute("SELECT * from restaurants WHERE NEIGHBORHOOD_ID = '1'")
db_cursor.execute("INSERT INTO restaurants (NAME, NEIGHBORHOOD_ID, PRICE_RANGE_ID) VALUES ('Mmahh', 1, 1)")
db_cursor.execute("INSERT INTO restaurants (NAME, NEIGHBORHOOD_ID, PRICE_RANGE_ID) VALUES ('AsiaBox', '1', '1')")
db_cursor.execute("INSERT INTO restaurants (NAME, NEIGHBORHOOD_ID, PRICE_RANGE_ID) VALUES ('Umami', '1', '1')")

# store the result in a local variable. 
# this will be a list of tuples, where each tuple represents a row in the table
list_restaurants = db_cursor.fetchall()

db_connection.commit()


db_connection.close()




