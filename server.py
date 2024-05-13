#tcp_server.py


import threading
from datetime import datetime
import socket

HOST = socket.gethostbyname(socket.gethostname()) #'localhost'
PORT = 16789

print("..HOST=...", HOST)


address = (HOST, PORT) 

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(address)
# server.listen()

# clients = []
# nicknames = []

# def broadcast(message):
# 	for client in clients:
# 		client.send(message)

# def handle(client):
# 	while True:
# 		try:
# 			message = client.recv(1024)
# 			broadcast(message)
# 		except:
# 			index = clients.index(client)
# 			clients.remove(client)
# 			client.close
# 			nickmane = nicknames[index]
# 			broadcast('{} left the chat!'.format(nickmane).encode('utf-8'))
# 			nicknames.remove(nickmane)
# 			break





# def receive():
# 	while True:
# 		client, address = server.accept()
# 		print('Connected with {}'. format(str(address)))
# 		#print(str(client))

# 		client.send( 'Nick'.encode('utf-8') )
# 		nickmane = client.recv(1024).decode('utf-8')
# 		nicknames.append(nickmane)
# 		clients.append(client)

# 		print('Nickmane of the client is {}'.format(nickmane))
# 		broadcast('{} joined the chat!'.format(nickmane).encode('utf-8'))
# 		client.sent('Connected to the server!'.encode('utf-8'))

# 		thread = threading.Thread(target=handle, args=(client,))
# 		thread.start()

# print('Server is listening....')
# receive()



# while True:
#        # establish a connection
#        clientsocket,addr = server.accept()      

#        print("Got a connection from %s" % str(addr))

#        msg = 'Thank you for connecting'+ "\r\n"
#        clientsocket.send(msg.encode('ascii'))
#        clientsocket.close()



'''
max_size = 1000

print('Starting the server-tcp at', datetime.now())
print('Waiting for a client to call.')


server.listen(5)
#listen сервер конфігурується так, щоб поставити в чергу
#п'ять клієнтських з'єднань перш, ніж відмовляти в наступному

client, addr = server.accept()
data = client.recv(max_size)    				
#виклик client.recv() встановлює max довжину вхідного повідомлення в байтах

print('At', datetime.now(), client, 'said', data)

client.sendall(b'Are you talking to me?')
client.close()
server.close()
'''
