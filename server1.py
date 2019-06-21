
import socket
import json

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("localhost", 12345))
serversocket.listen(1)

msg = """
HTTP/1.1
Content-Type: text/html

<html>
<body>
<b>Hello World</b>
<a href="/index.html">click me!</a>
</body>
</html>

"""
fh=open("mouse_log.txt","r")
str=fh.readline()
lis=str.split(" ",2)
data={}

data["date"]=lis[0]
data["time"]=lis[1]
data["action"]=lis[2]

while True:
    (clientsocket, address) = serversocket.accept()
    clientsocket.sendall(msg.encode('utf-8'))
    #output=json.dumps(dic)
    #clientsocket.sendall(output.encode('utf-8'))


    print("server sending reply") 
    #clientsocket.sendall(b"/n server received your message")
serversocket.close()
