import socket
import sys
import json

s = socket.socket()
print("Socket successfully created")

port = 8080

s.bind(('', port))
print("socket binded to " + str(port))

s.listen(5)
print("socket is listening")

file = open("Folder440.txt", "wb")
print("\nThe Folder that You Want to Copy at server is  Folder440.txt.\n")


while True:
	c, addr = s.accept()
	print("Got connection from" + str(addr))
	msg=("\nHello Client "+ addr[0] +" \n Thank You For Choosing This Server \n -Server?\n")
	c.send(msg.encode())
	buffer = c.recv(1024)
	while buffer:
		file.write(buffer)
		buffer =c.recv(1024)
		file.close()
		print("\nSuccessfully Copied! :)\n")


c.close()
