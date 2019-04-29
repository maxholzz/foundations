import sqlite3

# connect to the database file, and create a connection object
connection = sqlite3.connect('restaurantsBerlin.db')

# create a database cursor object, which allows us to perform SQL on the database. 
cursor = connection.cursor()

cursor.execute("SElECT * FROM restaurantsBerlin")

list_restaurants = cursor.fetchall()
print("list_restaurants contents:")
print(list_restaurants)


#sql_command = """
#CREATE TABLE restaurantsBerlin ( 
#R_number INTEGER PRIMARY KEY, 
#name VARCHAR(20));"""
#cursor.execute(sql_command)

#cursor.execute("INSERT INTO restaurantsBerlin (R_number, name) VALUES (1,'Mmahh')")
cursor.execute("SELECT * FROM restaurantsBerlin")

cursor = connection.cursor()

connection.commit()


connection.close()