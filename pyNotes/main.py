import mysql.connector
import defs

#conexão com o banco de dados
con = mysql.connector.connect(host='localhost', database='users', user='root', password='')
cursor = con.cursor()

defs.dbstart()

print('=-'*20)
print('Bem-vindo ao pyNotes 2.0, para iniciar faça o login ou cadastro.')
while True:
    print("Digite 1 para realizar o Cadastro ou 2 para fazer login.")
    choice = str(input("Escolha: "))
    if choice == '1':
        login = str(input("Login [Nome]: "))
        senha = str(input("Senha: "))
        print('Cadastro realizado com sucesso!')
        print('='*20)
    if choice == '2':
        print('login')

defs.end()
