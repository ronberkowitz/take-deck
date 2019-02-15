import socket


class Server:

    """ this class accepts new clients, adds them to open_clients and runs SessionWithClient
        in front of each new client.
    """

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server_socket = socket.socket()

        self.server_socket.bind((ip, port))
        self.server_socket.listen(1)

        self.open_clients = []

        print 'server {' + ip + ', ' + str(port) + '} is listening...'

    def close_server(self):
        self.server_socket.close()

    def __str__(self):
        return "server's IP: " + self.ip + "server's port" + str(self.port)