#!/usr/bin/env python
import socket
import os
import sys

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("Socket established")

port = sys.argv[1]

try:
    conn.bind(("127.0.0.1", int(port)))
    print("Connection bind successful")
except socket.error as msg:   
    print("Error: " + msg)
    sys.exit()
