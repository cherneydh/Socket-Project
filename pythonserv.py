#!/usr/bin/env python
import socket
import os
import sys

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("Socket established")

port = sys.argv[1]

try:
    serversocket.bind(('', int(port)))
    # queue up to 5 requests
    serversocket.listen(5)
    #serversocket.bind(("127.0.0.1", int(port)))
    print("Connection bind successful")
    print(socket.gethostname())
    print(int(port))
    #input("Press any key to continue.")
except socket.error as msg:
    print("Error: " + msg)
    sys.exit()
while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()
    print("Got a connection from %s" % str(addr))
    msg = 'Thank you for connecting'+ "\r\n"
    clientsocket.send(msg.encode('ascii'))
    query = clientsocket.recv(1024).decode("ascii")
    print("Command recieved: %s" % str(query))
    if (query == 'get'):
        print('test get')
    elif (query == 'put'):
        print('test put')
    elif (query == 'ls'):
        print('ls cmd')
        response = 'ls response' + "\r\n"
        clientsocket.send(response.encode('ascii'))
    elif (query == 'quit'):
        print("Closing connection from" % str(addr) )
        clientsocket.close()
    elif (query != 'quit'):
        print('Invalid command')
