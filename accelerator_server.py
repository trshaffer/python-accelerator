#! /usr/bin/env python3
import sys
import os
import socket
#Francis Schickel
#Goal: create Unix Domain Socket client/server model for fork code

server_address = '/tmp/accelerator_socket'

def socket_creation():
    try:
        os.unlink(server_address)
    #TODO: for right now, it must be a new socket
    #      Try to make it so this handles if the FD already exists and what to do w it
    except OSError:
        if os.path.exists(server_address):
            raise
    #If it gets here, there is no path that currently exists successfully
    #Create UDS socket
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    #Bind socket to port
    sock.bind(server_address)
    #listen for incoming connections
    sock.listen(1)
    return sock

if __name__ == "__main__":
    py_file = sys.argv[1]
    sock = socket_creation()
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
            print("finished connection with client")
            connection.close()

