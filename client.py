import socket
import os
import sys

server = sys.argv[1]
port = sys.argv[2]

print("Server: " + server + " Port: " + port)
query = ""

# create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
#host = socket.gethostname()
#port = 9999
# connection to hostname on the port.
try:
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(( server , int(port) ))
    print("Connection successfully completed")
except Exception as e:
    print(e)
    sys.exit()

# Receive test message
msg = clientsocket.recv(1024)
print (msg.decode('ascii'))

while (True):
    query = (input('ftp>')).lower()
    #send command to server
    clientsocket.send(query.encode('ascii'))
    if (query == 'get'):
        print('test get')

    elif (query == 'put'):
        print('test put')
        f = open(string(file),'rb')
        l = f.read(1024)
        while (l):
            print ('Sending')
            s.send(l)
            l = f.read(1024)
        f.close()
        clientsocket.shutdown(socket.SHUT_WR)
        clientsocket.recv(1024)
    elif (query == 'ls'):
        print('test ls')
        print (clientsocket.recv(1024).decode('ascii'))
    elif (query == 'quit'):
        print('Closing connection')
        clientsocket.send(query.encode('ascii'))
        clientsocket.close()
    elif (query != 'quit'):
        print('Invalid command')
