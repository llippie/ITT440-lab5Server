import socket
import sys
import json

s = socket.socket()
print("Socket successfully created")

port = 8080

try:
	s.bind(('', port))
	print("socket binded to " + str(port))
except:
	print("error bind")
	s.close
s.listen(5)
print("socket is listening..")

while True:
	c, addr = s.accept()
	print("Received file from" + str(addr))
	data = c.recv(1024)
	data = data.decode("utf-8")
	dataJ = json.loads(data)
	c.send(b"File received by the server.")
	file = open(dataJ.split("\n",1)[0],"w")
	file.write(dataJ.split("\n",1)[1])
c.close()
