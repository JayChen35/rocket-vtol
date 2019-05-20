import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.1.154', 5005))
sock.listen()

conn, addr = sock.accept()
# print("Host address: ", addr, "Port: ", port)\
msg = "this is a test"
conn.send(msg.encode('utf-8'))
print("sent")
sock.shutdown(socket.SHUT_RDWR)
sock.close()
# print("Connection terminated.")
