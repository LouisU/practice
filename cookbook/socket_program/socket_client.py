# -*- coding: utf-8 -*-
# author = "Louis"
import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8000))

while True:

    data = input()
    client.send(data.encode('utf8'))
    if data == 'exit!':
        client.close()
        break
    rec_data = client.recv(1024)
    print(rec_data.decode('utf8'))
