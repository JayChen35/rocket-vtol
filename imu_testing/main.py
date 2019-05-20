import time
import threading
import socket

from smbus2 import SMBusWrapper

SLAVE_ADDRESS = 0x04

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
    main()
