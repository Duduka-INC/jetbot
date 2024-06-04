# first of all import the socket library
import socket
import random
import time
# next create a socket object
s = socket.socket()
print("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 6666

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print("socket binded to %s" % (port))
print(socket.gethostbyname(socket.gethostname()))
# put the socket into listening mode
s.listen()
print("socket is listening")
c, addr = s.accept()
print('Got connection from', addr)

while True:
    # Establish connection with client.

    # send a thank you message to the client. encoding to send byte type.
    #c.send(random.choice(arr).encode())
    print(val := [random.uniform(-0.9, 0.9), random.uniform(-0.9, 0.9)].encode())
    c.send(val)

    # Close the connection with the client
    # Breaking once connection closed
    # break