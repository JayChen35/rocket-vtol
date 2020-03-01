import struct
import smbus2 as smbus

ADDR = 0x04

bus = smbus.SMBus(1)

def bytes_to_float(data):
    return struct.unpack('f', data)[0]

def read():
    data = bus.read_i2c_block_data(ADDR, 0x00, 8)
    data = bytes(data)
    inchesX = bytes_to_float(data[0:4])
    inchesY = bytes_to_float(data[4:8])
    return inchesX, inchesY

def write(data):
    bus.write_byte(ADDR, data)

while True:
    inp = input()
    if inp == "R":
        print(read())
    else:
        write(int(inp))