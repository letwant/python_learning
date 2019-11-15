import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# # 绑定端口:
# s.bind(('127.0.0.1', 9999))
#
# print('Bind UDP on 9999...')
# while True:
#     # 接收数据:
#     data, addr = s.recvfrom(1024)
#     print('Received from %s:%s.' % (addr, data))
#     s.sendto(b'Hello, %s!' % data, addr)


# import sys
#
# HOST, PORT = "localhost", 9999
# data = " ".join(sys.argv[1:])
#
# # SOCK_DGRAM is the socket type to use for UDP sockets
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# # As you can see, there is no connect() call; UDP has no connections.
# # Instead, data is directly sent to the recipient via sendto().
# sock.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
# received = str(sock.recv(1024), "utf-8")
#
# print("Sent:     {}".format(data))
# print("Received: {}".format(received))
#
# import socketserver
#
# class MyUDPHandler(socketserver.BaseRequestHandler):
#     """
#     This class works similar to the TCP handler class, except that
#     self.request consists of a pair of data and client socket, and since
#     there is no connection the client address must be given explicitly
#     when sending data back via sendto().
#     """
#
#     def handle(self):
#         data = self.request[0].strip()
#         socket = self.request[1]
#         print("{} wrote:".format(self.client_address[0]))
#         print(data)
#         socket.sendto(data.upper(), self.client_address)
#
# if __name__ == "__main__":
#     HOST, PORT = "localhost", 9999
#     server = socketserver.UDPServer((HOST, PORT), MyUDPHandler)
#     server.handle_timeout()
#     server.serve_forever()


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for data in [b'Michael', b'Tracy', b'Sarah']:
        # 发送数据:
        s.sendto(data, ('127.0.0.1', 6666))
        # 接收数据:
        print(s.recv(1024).decode('utf-8'))
    s.close()