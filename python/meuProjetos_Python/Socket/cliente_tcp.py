from socket import *

server = "127.0.0.1"
port = 1010

msg = bytes(input("digite algo: "), 'utf-8')
obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.connect((server, port))
obj_socket.send(msg)

resposta = obj_socket.recv(1024)
print("recebi: ", resposta)
obj_socket.close()