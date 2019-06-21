import socket

#socket.SOCK_STREAM indicates TCP
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(("localhost", 12345))

msg = "Hello World from client"

print("client sending: "+msg)
clientsocket.send(msg.encode())
