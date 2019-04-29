#!/Users/lucca/AppData/Local/Programs/Python/Python37-32

# A simple script to accept input from an html form,
# parse the information, and do something - which in this case
# is to give user feedback with a simple html page.

# use python's the CGI package
import cgi
import sys

# get the output of the form.
form = cgi.FieldStorage()

# get an input filed from the form called 'first_name'
# and assign it's value to a local variable called first_name
first_name = form.getvalue('first_name')

# send an html response.
print("""
<html>
<body>
<p>
Thanks %s, that worked. :)
</p>
</body>
</html>
"""% first_name)