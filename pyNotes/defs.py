import mysql.connector

def dbstart():
    con = mysql.connector.connect(host='localhost', database='users', user='root', password='')
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS LOGIN(
	LOGIN VARCHAR(20) NOT NULL PRIMARY KEY,
    SENHA VARCHAR(20) NOT NULL
);""")

def signup(login, senha):
    con = mysql.connector.connect(host='localhost', database='users', user='root', password='')
    cursor = con.cursor()
    cursor.execute(f"INSERT INTO LOGIN VALUES('{login}', '{senha}');")
    cursor.execute(f"SELECT * FROM LOGIN WHERE LOGIN = '{login}' AND SENHA = '{senha}';")
    user = cursor.fetchone()
    if user is not None:
        print(f"Cadastro realizado com sucesso! Seja bem-vindo {login}.")

def end():
    con.close()
    cursor.close()