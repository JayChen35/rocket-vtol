import socket
import time
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.1.154', 5005))

from_server = sock.recv(4096).decode('utf-8')
time.sleep(1)
print(from_server)
time.sleep(3)
from_server2 = json.loads(sock.recv(4096))  # .decode('utf-8')?
print(from_server2)
print(from_server2['hi'])
sock.close()
