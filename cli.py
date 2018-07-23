#!/usr/bin/env python
import socket
import os
import sys

server = sys.argv[1]
port = sys.argv[2]
print("Server: " + server + " Port: " + port)
query = ""

while(query != "quit"):
    query = raw_input("ftp> ")
