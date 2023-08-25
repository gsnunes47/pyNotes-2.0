import mysql.connector
import defs

#Conexão com o banco de dados
con = mysql.connector.connect(host='localhost', database='users', user='root', password='')
cursor = con.cursor()

#Verificação da existencia da table de usuários
defs.dbstart()

print('=-='*20)
print('Bem-vindo ao pyNotes 2.0, para iniciar faça o login ou cadastro.')
while True:
    print("Digite 1 para realizar o Cadastro ou 2 para fazer login.")
    choice = str(input("Escolha: "))
    
    #Cadastro
    if choice == '1':
        login = str(input("Login: "))
        senha = str(input("Senha: "))
        defs.signup(login, senha)
        print('=-='*20)
    
    #Login
    if choice == '2':
        login = str(input("Login: "))
        confirmação = defs.signin(login)
        if confirmação == True:
            print('=-='*20)
            break

print('Notas')

defs.end()
