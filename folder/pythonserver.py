#!/usr/bin/env python
import socket
import os
import sys
import subprocess

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
    # establish a connection
    clientsocket,addr = serversocket.accept()
    print("Got a connection from %s" % str(addr))
    msg = 'Thank you for connecting'+ "\r"
    clientsocket.send(msg.encode('ascii'))
except socket.error as msg:
    print("Error: " + msg)
    sys.exit()
while True:
    try:
        query = clientsocket.recv(1024).decode("ascii")
    except OSError:
        print ("Client disconnected")
        break
    print("Command recieved: %s" % str(query))
    if (query == 'get'):
        filename = clientsocket.recv(1024).decode("ascii")
        print(filename) 
    elif (query == 'put'):
        filename = clientsocket.recv(1024).decode("ascii")
        print(filename)
        f = open(filename, 'wb')
        l = clientsocket.recv(1024)
        while (l):
            f.write(l)
            l = clientsocket.recv(1024)
    elif (query == 'ls'):
        print('ls cmd')
        response = 'ls response' + "\r\n"
        ls = os.listdir()
        string = '\n'.join(ls)
        response = response + string
        clientsocket.send(response.encode('ascii'))
        #clientsocket.send(' '.join(os.listdir(os.curdir)).encode('ascii'))
    elif (query == 'quit'):
        print("Closing connection from: %s" % str(addr) )
        clientsocket.close()
    elif (query != 'quit'):
        print('Invalid command')
