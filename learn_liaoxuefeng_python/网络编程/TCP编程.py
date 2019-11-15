from socketserver import ThreadingMixIn, UDPServer, BaseRequestHandler
import threading

class UdpSocketServer(UDPServer, ThreadingMixIn):
    pass


class Handler(BaseRequestHandler):

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        socket.sendto(data.upper(), self.client_address)


if __name__ == '__main__':
    server = UdpSocketServer(('127.0.0.1', 6666), Handler)
    server_thread = threading.Thread(target=server.serve_forever())
    server_thread.daemon = True
    server_thread.start()