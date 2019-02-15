import threading


MAX_DATA_LENGTH = 1024


class ClientHandle(threading.Thread):

    """ this class acts in front of each client. (sends messages, gets messages, adds to database, etc.) """

    def __init__(self, server, client_socket, client_address):
        threading.Thread.__init__(self)
        self.server = server
        self.client_socket = client_socket
        self.client_address = client_address

    # =======================================================

    def get_message(self):
        data = self.client_socket.recv(MAX_DATA_LENGTH)
        print "got message "
        return data

    def send_message(self, message):
        print "sending %s" % message
        self.client_socket.send(message)

    # ========================================================
    def close_client(self):
        self.client_socket.close()

    # ========================================================

    def run(self):
        """ Start handling the client """
        print self.get_message()
        self.send_message('ze swissa ahi');

