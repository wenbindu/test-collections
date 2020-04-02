import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('0000', 8000))
server.listen()
sock, addr = server.accept()

data = sock.recv(1024)
print(data.decode('utf8'))
sock.send('boddy'.encode('utf8'))
server.close()
sock.close()
