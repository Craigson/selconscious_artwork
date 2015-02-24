# http://www.binarytides.com/python-socket-server-code-example/
# https://github.com/Uberi/speech_recognition#readme

#imports for server
import socket

#imports for jacobian functions
import scipy
import math
from scipy.special import ellipj

r = 50
a = 0.5
x = []
y = []
z = []

#ellipj returns sn,cn,dn,ph

for t in range(1,101):
	jacobi = scipy.special.ellipj(t,(a*a))
	x.append(r * (jacobi[0])*math.cos(a*t))
	y.append(r * (jacobi[0])*math.sin(a*t))
	z.append(r * jacobi[1])


def Main():
	print("server started, listening for connection...")
	host = "127.0.0.1"
	port = 5001

	s = socket.socket()
	s.bind((host,port))

	s.listen(1)
	c, addr = s.accept()
	print('connection from: ' + str(addr))

	i = 0

	while False:
		# outgoing ='A'
		# c.send(outgoing)
		print("waiting...")

	while True:
		data = c.recv(1024)
		print(data)
		c.send("hello")
		if not data:
			break

		if data == 'A':
			outgoing = x[i]
			i+=1

		# if outgoing == 'q':
		# 	c.close()

		print("sending: " + str(x[i]))
		# data = str(data).upper()
		# print ("sending: " + str(data))
		c.send(outgoing)

	c.close()



if __name__ == '__main__':
	Main()
