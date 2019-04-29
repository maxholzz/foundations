#!/usr/bin/python


import cgi
import sys
import csv


form = cgi.FieldStorage()


user_color = form.getvalue('color')
    
with open('colors.csv') as _filehandler:
    csv_file_reader = csv.reader(_filehandler)
    check = False
    for row in csv_file_reader:
        if user_color.title() == row[1]:
        	check = True
        	break
    if check == True:
    	print("""
    		<!DOCTYPE html>
			<html>
			<style>
			body{background-color: %s} 
			</style>
			<head>
			<title> Server Answer </title>
			</head>
			<body>
			<br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br>
			<p style="text-align:center;font-size:40px"> Wow %s is such a cool color! The Hexcode for it is: %s </p>
			</body>
			</html>
    		"""%(row[2], user_color ,  row[2]))
    if check == False:
    	print("""
    		<!DOCTYPE html>
			<html>
			<head>
			<title> Answer </title>
			</head>
			<body>
			<p> %s is not color idiot!</p>
			</body>
			</html>
    		"""% user_color)