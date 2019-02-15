# -*- coding: utf-8 -*-
import socket
from wrappers.server_wrapper import Server
from clientHandle import ClientHandle

# import SWC
# from database import SOKDatabase


SERVER_IP = '127.0.0.1'
SERVER_PORT = 4378


def main():
    """
    Add Documentation here
    """
    pass  # Add Your Code Here
    server = Server(SERVER_IP, SERVER_PORT)
    while True:
        client_socket, client_address = server.server_socket.accept()
        new_client = ClientHandle(server=server, client_socket=client_socket, client_address=client_address)
        server.open_clients.append(new_client)
        print 'new client joined: %s. current number of clients is %s' % (client_address, len(server.open_clients))
        new_client.start()


if __name__ == '__main__':
    main()