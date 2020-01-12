import smbus2
import smbus
from smbus2 import SMBusWrapper 
import time
import struct
 
# Slave Addresses for Arduinos 
SLAVE_ADDRESS = 0x40
 
# Create the I2C bus 
while True:
    with SMBusWrapper(1) as bus:
        cmd = "send_ultrasonic_data"
        # byte_array = str_to_byte_array(cmd)
        byte_array = cmd.encode("utf-8")
        bus.write_i2c_block_data(SLAVE_ADDRESS, 0x10, byte_array)
        print("Data sent.")
        time.sleep(0.1)
        # block = bus.read_i2c_block_data(SLAVE_ADDRESS, 0, 4)
        # print(block)
        # data = struct.unpack('f', bytearray(block))[0]
        # data = struct.unpack('<l', block)
        # print(data)
        data = bus.read_byte(SLAVE_ADDRESS, 0)
        print(data)
        example = b"\x64\xd8\x64\x3f"
        print(struct.unpack('f', example)[0])
    time.sleep(1)

"""
bus = smbus.SMBus(1)

def get_data():
    return bus.read_i2c_block_data(SLAVE_ADDRESS, 0)

def get_float(data, index):
    byte_array = data[4*index:(index+1)*4]
    return struct.unpack('f', bytes(byte_array))[0]

while True:
    data = get_data()
    print(get_float(data,0))
    print(get_float(data,1))
    time.sleep(1)
"""
