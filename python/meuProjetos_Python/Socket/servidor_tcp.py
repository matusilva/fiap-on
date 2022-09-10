from socket import *

server = "127.0.0.1"
port = 1010

obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((server, port))
obj_socket.listen(2)

print("Aguardando cliente...")

while True:
    con, cliente = obj_socket.accept()
    print("conectando com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024))
        print("Recebi: ", msg_recebida)
        msg_enviada = b'ola cliente'
        con.send(msg_enviada)
        break
    con.close()