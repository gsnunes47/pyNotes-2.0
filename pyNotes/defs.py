import mysql.connector

def dbstart():
    con = mysql.connector.connect(host='localhost', database='users', user='root', password='')
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS LOGIN(
	LOGIN VARCHAR(20) NOT NULL PRIMARY KEY,
    SENHA VARCHAR(20) NOT NULL,
    NOTAS TEXT
);""")

def signup(login, senha):
    con = mysql.connector.connect(host='localhost', database='users', user='root', password='')
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM LOGIN WHERE LOGIN = '{login}';")
    row = cursor.fetchone()
    if row == None:
        cursor.execute(f"INSERT INTO LOGIN (LOGIN, SENHA) VALUES('{login}', '{senha}');")
        cursor.execute(f"SELECT * FROM LOGIN WHERE LOGIN = '{login}' AND SENHA = '{senha}';")
        user = cursor.fetchone()
        if user is not None:
            print(f"Cadastro realizado com sucesso! Seja bem-vindo {login}.")
    else:
        print("Login já cadastrado, tente utilizar outro nome.")

def signin(login):
    con = mysql.connector.connect(host='localhost', database='users', user='root', password='')
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM LOGIN WHERE LOGIN = '{login}';")
    user = cursor.fetchone()
    if user != None:
        if login in user:
            strike = 0
            while strike != 3:
                senha = str(input("Senha: "))
                if senha in user:
                    print(f"Login realizado com sucesso! Seja bem-vindo {login}.")
                    break
                else:
                    strike += 1
                    if strike <= 2:
                        print('Senha Incorreta, tente novamente.')
                    elif strike == 3:
                        print('Você digitou a senha incorreta muitas vezes.')
                        exit()
                        return False        
    else:
        print('Usuário não encontrado, faça o cadastro ou tente novamente.')
        return False
    return True

def updatenotes(user, text):
    con = mysql.connector.connect(host='localhost', database='users', user='root', password='')
    cursor = con.cursor()
    cursor.execute(f"UPDATE LOGIN SET NOTAS = '{text}' WHERE LOGIN = '{user}';")

def end():
    con = mysql.connector.connect(host='localhost', database='users', user='root', password='')
    cursor = con.cursor()
    con.close()
    cursor.close()
