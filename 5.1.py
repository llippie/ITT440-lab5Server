import socket

#commented for UDP
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket done")
port=8888
#ip= '192.168.56.102'
s.bind(('',port))
print("Bind done with port "+str(port))
#message = b'Thanks'
#s.sendto(message,(ip,port))
#buffer,addr = s.recvfrom(1024)
#print(buffer)
s.listen(5)
print("Listening...")

while True:
	c,addr = s.accept()
	print("Connected to "+str(addr))
	c.send(b'Thanks')
	buffer = c.recv(1024)
	print(buffer)
c.close()
s.close()
