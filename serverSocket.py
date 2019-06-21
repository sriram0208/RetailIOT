import socket

#socket.SOCK_STREAM indicates TCP
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("localhost", 12345))
serversocket.listen(5)

(clientsocket, address) = serversocket.accept()
msg = clientsocket.recv(1024)
print("server recieved "+msg.decode())
