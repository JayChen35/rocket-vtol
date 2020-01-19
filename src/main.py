import smbus
#from smbus2 import SMBusWrapper 
import time
import struct
 
# Slave Addresses for Arduinos
SLAVE_ADDRESS = 0x4
bus = smbus.SMBus(1)

# Create the I2C bus 
while True:
    block = bus.read_i2c_block_data(SLAVE_ADDRESS, 0x10, 4)
    ultra1 = float(str(block[0]) + '.' + str(block[1]).zfill(2))
    ultra2 = float(str(block[2]) + '.' + str(block[3]).zfill(2))
    print(str(ultra1) + " " + str(ultra2))
    time.sleep(.1)

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
