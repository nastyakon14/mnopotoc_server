import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8080       # The port used by the server
conn = socket.socket()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
client_socket.close()
print('Received', repr(data))