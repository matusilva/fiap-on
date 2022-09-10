from socket import *

server = "127.0.0.1"
port = 1010

obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.connect((server, port))
saida = ""

while saida != "X":
    msg = input("digite algo: ")
    obj_socket.sendto(msg.encode(), (server, port))
    dados, origem = obj_socket.recvfrom(65535)
    print("recebi: ", dados.decode())
    saida = input("digite <x> para sair: ").upper()

obj_socket.close()