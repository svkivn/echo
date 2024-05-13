#tcp_client.py 

import socket
import threading
from datetime import datetime


nickmane = input('Choose a nickname: ')

#HOST = socket.gethostbyname("https://echo-fxx2.onrender.com") #'localhost'
address = ("44.226.145.213", 10000)

print('Starting the client at', datetime.now())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)		#встановити потік







def receive():
	while True:
		try:
			message = client.recv(1024).decode('utf-8')
			if message == "NICK":
				client.send(nickmane.encode('utf-8'))
			else:
				print(message)
		except:
			print('Error occurred!')
			client.close()
		break

def write():
	while True:
		message = '{}: {}'.format(nickmane, input(''))
		client.send(message.encode('utf-8'))



receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()		


 
