from socket import *

server = "127.0.0.1"
port = 1010

obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.bind((server, port))

print("Servidor pronto...")

while True:
    dados, origem = obj_socket.recvfrom(65535)
    print("Origem...........: ", origem)
    print("Dados............: ", dados.decode())
    resposta = input("Digite a resposta: ")
    obj_socket.sendto(resposta.encode(), origem)

obj_socket.close()
