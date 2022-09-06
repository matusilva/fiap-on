from Dicionarios.Funcoes import *

users = {}

opcao = menu()
while opcao == "i" or opcao == "p" or opcao == "e" or opcao == "l":
    if opcao == "i":
        inserir(users)
    opcao = menu()