import socket
import sys
import json

mydata={"id":505012,"name":"Azizi","age":"29"}
sendData=json.dumps(mydata)

s=socket.socket()
print("Socket created")
port =8080

s.bind(('',port))
print("Socket Binded to "+str(port))
s.listen(5)
print("Listening...")

while True:
	c,addr = s.accept()
	print("Connected to "+str(addr))

	c.sendall(bytes(sendData,encoding="utf-8"))
	buffer = c.recv(1024)
	print(buffer)
c.close()
