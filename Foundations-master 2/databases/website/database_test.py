# import function from database connect file 
from database_connect import get_restaurants

# pass a variable to the function, call a SQL query based on it, and get a returned. 
l = get_restaurants("Kreuzberg")
for restaurant in l:
        print(restaurant[1])
