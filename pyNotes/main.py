import mysql.connector
import defs

con = mysql.connector.connect(host='localhost', database='users', user='root', password='')
cursor = con.cursor()

if con.is_connected():
    print('working')

defs.end()
