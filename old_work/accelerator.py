#! /usr/bin/env python3
import socket
import sys
import os
from daemonize import Daemonize

def daemon_server():
    server_address = '/tmp/accelerator_socket'
    #py_file = sys.argv[1]
    try:
        os.unlink(server_address)
    #TODO: for right now, it must be a new socket
    #      Try to make it so this handles if the FD already exists and what to do w it
    except OSError:
        if os.path.exists(server_address):
            raise
    #If it gets here, there is no path that currently exists successfully
    #Create UDS socket
def thing():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    #Bind socket to port
    sock.bind(server_address)
    #listen for incoming connections
    sock.listen(1)
    while True:
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('connection from: ', client_address)
            while True:
                data = connection.recv(16)
                print(data.decode(), end='')
                if data:
                    connection.sendall(data)
                else:
                    print('no more data from: ', client_address)
                    break
            print("")
        finally:
            connection.close()

def try_this():
    daemon = Daemonize(app="test_app", pid='/tmp/accelerator_pid_file.pid', action=daemon_server)
    daemon.start()

    


if __name__ == "__main__":
    daemon_server()
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
            data = sock.recv(16)
            amount_received += len(data)
            print('received "%s"' % data)

    finally:
        print('closing socket')
        sock.close()
    #daemon.exit()
