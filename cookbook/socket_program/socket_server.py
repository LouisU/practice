# coding=utf-8
# Author="Louis"

# import socket
# This is a practise of one server only for one client.
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(('0.0.0.0', 8000))
# server.listen()
# sock, addr = server.accept()
#
# while True:
#
#     recv_data = sock.recv(1024)
#     print(recv_data.decode('utf8'))
#     send_data = input()
#     sock.send(send_data.encode('utf8'))
#     #server.close()
# sock.close()

import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8000))
server.listen()


def open_one_socket(sock, addr):
    while True:
        recv_data = sock.recv(1024)
        print(recv_data.decode('utf8'))
        if recv_data.decode('utf8') == 'exit!':
            break
        send_data = input()
        sock.send(send_data.encode('utf8'))
    sock.close()


while True:
    sock, addr = server.accept()
    client_thread = threading.Thread(
        target=open_one_socket, args=(sock, addr))
    client_thread.start()
