# http://www.binarytides.com/python-socket-server-code-example/
# https://github.com/Uberi/speech_recognition#readme

import socket

def Main():
	host = "127.0.0.1"
	port = 5001

	s = socket.socket()
	s.bind((host,port))

	s.listen(1)
	c, addr = s.accept()
	print('connection from: ' + str(addr))

	while True:
		data = c.recv(1024)
		print(data)
		if not data:
			break
		outgoing = raw_input(">> ")
		if outgoing == 'q':
			c.close()

		print("from connected user: " + str(data))
		# data = str(data).upper()
		# print ("sending: " + str(data))
		c.send(outgoing)

	c.close()

if __name__ == '__main__':
	Main()
