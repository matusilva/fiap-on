users = {}
emails = ["xpto@xyz.com", "xkcd@phd.com"]

tupla = list(enumerate(emails))

for chave in range(0, len(tupla)):
    print("Email: ", tupla[chave][1])
    users[tupla[chave]] = [input("Nome: "), input("Nível: ")]

for chave, dado in users.items():
    print("Usuario.:", chave[0])
    print("Email...:", chave[1])
    print("Nome....:", dado[0])
    print("Nível...:", dado[1])