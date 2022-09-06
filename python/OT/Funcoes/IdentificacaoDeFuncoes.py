def preencherInventario(lista):
    resp = "S"
    while resp == "S":
        equipamento = [input("Equipamento: "), float(input("Valor: "))]
        lista.append(equipamento)
        resp = input("Digite \"S\" para continuar: ").upper()

def exibirInventario(lista):
    for elemento in lista:
        print("\nNome....: ", elemento[0])
        print("Valor...: ", elemento[1])

def buscarPorNome(lista):
    busca = input("\nDigite o nome para buscar: ")
    for elemento in lista:
        if busca == elemento[0]:
            print("Nome...: ", elemento[0])
            print("Valor..: ", elemento[1])

