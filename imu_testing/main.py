import time
import threading
import socket

from smbus2 import SMBusWrapper

SLAVE_ADDRESS = 0x04
SERVER_ADDRESS = '192.168.1.35'
PORT = 5005

def init():
    global sock, conn, addr
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((SERVER_ADDRESS, PORT))
    sock.listen()
    conn, addr = sock.accept()


def main():
    start = threading.Thread(target=startup, daemon=True)
    command = threading.Thread(target=command_ingest, daemon=True)
    start.join()

def startup():
    # Pull first batch of IMU data, move servo 360 degrees
    pass

def command_ingest():
    while True:
        pass

def send_data(cmd):
    byte_data = COMMAND_SET[cmd]
    with SMBusWrapper(1) as bus:
        bus.write_byte_data(SLAVE_ADDRESS, 0, byte_data)
    print("Data (", byte_data, ") sent.")

def read_data():
    length = 1
    with SMBusWrapper(1) as bus:
        data = bus.read_i2c_block_data(SLAVE_ADDRESS, 0, length)
    print("Data received: \n", data)

if __name__ == "__main__":
    init()
    main()
