import serial
import time

ser = serial.Serial('COM17', baudrate=9600, timeout=0)
while True:
    ser.write(b"hi")
    time.sleep(1)