#! /usr/bin/env python3
import socket
import sys
import os
import time

def daemon_server():
    server_address = '/tmp/accelerator_socket'
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
            print("close server connection to client")
            connection.close()

def fork_creation():
    print("fork creation function")
    pid = os.fork()
    if pid == 0:
        print("hello there!")
        os.setsid()
        daemon_server()
    else:
        time.sleep(5)
        return

if __name__ == "__main__":
    # Create a UDS socket
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = '/tmp/accelerator_socket'
    print('connecting to %s' % server_address)
    
    if os.path.exists(server_address):
        print("path exists")
        try:
            print("trying to connect")
            sock.connect(server_address)
        except Exception:
            print("connect failed sadly")
            os.unlink(server_address)
            fork_creation()
            sock.connect(server_address)
    else:
        print("path does not exist")
        fork_creation()
        sock.connect(server_address)

    try:
        
        # Send data
        message = 'This is the message.  It will be repeated.'
        msgg = str.encode(message)
        print('sending "%s"' % message)
        sock.sendall(msgg)
        print("do i sendall?")

        amount_received = 0
        amount_expected = len(message)
        print(amount_received, " and ", amount_expected)
        
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print('received "%s"' % data)

    finally:
        print('closing socket')
        sock.close()
