import mysql.connector

cnx = mysql.connector.connect(user='root', 
    password='MyNewPass',
    host='127.0.0.1',
    database='education',
    auth_plugin='mysql_native_password')

# ----------------------------------- 
#           YOUR CODE
# ----------------------------------- 

college = input('Enter College Name:')
students = input('Enter student Population:')

cursor = cnx.cursor()
query = ()
