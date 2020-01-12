import smbus2
from smbus2 import SMBusWrapper 
import time
 
# Slave Addresses for Arduinos 
SLAVE_ADDRESS = 0x40
 
# Create the I2C bus 
while True:
    with SMBusWrapper(1) as bus:
        cmd = "send_ultrasonic_data"
        # byte_array = str_to_byte_array(cmd)
        byte_array = cmd.encode("utf-8")
        bus.write_i2c_block_data(SLAVE_ADDRESS, 0x01, byte_array)
        print("Data sent.")
        val_received = bus.read_i2c_block_data(SLAVE_ADDRESS, 0x01, 4)
		print(val_received)
    time.sleep(1)

# This function converts a string to an array of bytes. 
def str_to_byte_array(string: str): 
    converted = [] 
    for char in string: 
        converted.append(ord(char))  
    return converted</pre>
