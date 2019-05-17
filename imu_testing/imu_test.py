import smbus
import time
import struct

from smbus2 import SMBusWrapper

COMMAND_SET = {
    'data': 0,
    'status': 1,
    'servo' : 2,
    'shutdown': 3
}
SLAVE_ADDRESS = 0x04

def main():
    while True:
        cmd = input("Send command (0) or pull data (1): ")
        if cmd == "0":
            print("Command set: ")
            to_print = ""
            for key, _ in COMMAND_SET.items():
                to_print += key + ", "
            to_print = to_print[:-2]
            print("{", to_print, "} \n")
            while True:
                temp = input("Send what command? ")
                if temp in COMMAND_SET:
                    send_data(temp)
                    break
                else:
                    print("Invalid command.")
            break
        elif cmd == "1":
            read_data()
            break
        else:
            print("Try again.")

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
