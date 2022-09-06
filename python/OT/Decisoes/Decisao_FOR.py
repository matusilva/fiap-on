numero = int(input("Digite um numero: "))
print("Tabuada de ", numero)
for valor in range(0, 11, 1): # valor inicial, valor limite, valor do incremento
    print(str(numero) + " x " + str(valor) + " = " + str(numero * valor))