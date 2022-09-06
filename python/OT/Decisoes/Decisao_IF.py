nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_contagiosa = input("Suspeita de doença contagiosa? ").upper()

if idade >= 65:
    print("O paciente " + nome + " POSSUI atendimento prioritário!")
elif doenca_contagiosa == "SIM":
    print("O paciente " + nome + " deve ser direcionado para sala de espera reservada.")
else:
    print("O paciente " + nome + " NÃO possui atendimento prioritário!")