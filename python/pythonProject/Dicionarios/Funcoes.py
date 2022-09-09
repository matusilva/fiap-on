def menu():
    return input("O que deseja realizar?\n" +
                  "| i | - inserir\n" +
                  "| p | - pesquisar\n" +
                  "| e | - excluir\n" +
                  "| l | - listar\n").lower()

def inserir(dicionario):
    dicionario[input("Login: ").lower()] = [input("Nome: "),
                                       input("ultima data de acesso: "),
                                       input("ultima estação acessada: ")]
    salvar(dicionario)

def salvar(dicionario):
    with open("db.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write("\n"+chave + ":" + str(valor))
