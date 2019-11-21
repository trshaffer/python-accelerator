#! /usr/bin/env python3
import socket
import sys
import os
from daemonize import Daemonize

if __name__ == "__main__":
    # Create a UDS socket
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = '/tmp/accelerator_socket'
    print('connecting to %s' % server_address)
    try:
        sock.connect(server_address)
    except Exception as msg:
        print(msg)
        sys.exit(1)
    try:
        
        # Send data
        message = 'This is the message.  It will be repeated.'
        msgg = str.encode(message)
        print('sending "%s"' % message)
        sock.sendall(msgg)
        amount_received = 0
        amount_expected = len(message)
        
        while amount_received < amount_expected:
            print("1sending still")
            data = sock.recv(16)
            print("2sending still")
            amount_received += len(data)
            print('received "%s"' % data)

    finally:
        print('closing socket')
        sock.close()
    #daemon.exit()
