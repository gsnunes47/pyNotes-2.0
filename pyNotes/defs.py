import mysql.connector

def dbstart():
    con = mysql.connector.connect(host='localhost', database='users', user='root', password='')
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS LOGIN(
	LOGIN VARCHAR(20) NOT NULL PRIMARY KEY,
    SENHA VARCHAR(20) NOT NULL
);""")

# def signup():


def end():
    con.close()
    cursor.close()