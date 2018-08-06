# Socket-Project
Socket Project for CPSC 471

Daniel Cherney - cherneydh@csu.fullerton.edu

Devin  Cao     - devincao@csu.fullerton.edu

Hamesh Sharma  - hksharma@csu.fullerton.edu


What kinds of messages will be exchanged across the control channel?

push, pull, ls, quit

How should the other side respond to the messages?

ACKs

What sizes/formats will the messages have?

Padding messages so they are the same size

What message exchanges have to take place in order to setup a file transfer channel?

3 Way Handshake

How will the receiving side know when to start/stop receiving the file?

Header information

How to avoid overflowing TCP buffers?

Check the current packet size against buffer size

This project was written in Python3.

How to execute:

python3.5 pythonserver.py 13371

python3.5 client.py 127.0.0.1 13371

Additional Notes:
