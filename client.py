import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
client_socket.connect(("localhost", 10000))

while True:
    data = client_socket.recv(1024)
    print(data.decode())
