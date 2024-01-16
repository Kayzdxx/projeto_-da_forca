# 1 - Faça um programa que leia um nome de usuário e a sua 
#  senha e não aceite a senha igual ao nome do usuário, mostrando uma 
#  mensagem de erro e voltando a pedir as informações.



while True :

    user = input("Digite seu nome de usuario : ")
    password = input("digite sua senha: ")
    

    if user != password :
        print("acesso permitido!")
        break
    print("senha e usuario iguais, tente novamente: ")













