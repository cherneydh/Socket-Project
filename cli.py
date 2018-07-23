#!/usr/bin/env python
import socket
import os
import sys

from socket import *

server = sys.argv[1]
port = sys.argv[2]
print("Server: " + server + " Port: " + port)
query = ""

try:
    cliconn = socket(AF_INET, SOCK_STREAM)
    cliconn.connect(( server , int(port) ))
    print("Connection successfully completed")
except Exception, e:
    print(e)
    sys.exit()

while(query != "quit"):
    query = raw_input("ftp> ")
