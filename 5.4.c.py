import json
import sys
import socket

s = socket.socket()

port = 8080

s.connect(('192.168.56.104', port))

print("Select The File That You Want To Sent :)")
file = input("File Name:")
print("File Name: " + file)

document = open(file, "rb")
DataTransf = document.read(1024)

while DataTransf:

	print("\nThe Message Received from the server are\n",s.recv(1024).decode("utf-8"))
	s.send(DataTransf)
	DataTransf = document.read(1024) 


s.close()
