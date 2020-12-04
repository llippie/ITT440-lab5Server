import socket
import os
from _thread import*

s = socket.socket()
host=''
port =8889
ThreadCount=0
try:
	s.bind((host,port))
except socket.error as e:
	print(str(e))

print("Waiting for connection...")
s.listen(5)

def threaded_client(connection):
	connection.send(str.encode("Welcome Genshin Global server\n"))
	while True:
		data = connection.recv(2048)
		reply = "Server said: "+data.decode('utf-8')
		if not data:
			break
		connection.sendall(str.encode(reply))
	connection.close()

while True:
	Client, address = s.accept()
	print("Connected to: "+address[0]+":"+str(address[1]))
	start_new_thread(threaded_client,(Client,))
	ThreadCount+=1
	print("Thread Number: "+str(ThreadCount))
s.close()
