'''
Created on Sep 16, 2013

@author: 521051
'''
from bluetooth import *

# Create the client socket
client_socket=BluetoothSocket( RFCOMM )

client_socket.connect(("7C:6D:62:98:16:11", 3))

 #---> 00:AA:70:18:DA:62
 #---> 7C:6D:62:98:16:11

client_socket.send("Hello World")

print "Finished"

client_socket.close()