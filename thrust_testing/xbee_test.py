import serial
import time

ser = serial.Serial('COM15', baudrate=9600, timeout=0)
while True:
    inp = input()
    ser.write(inp.encode())
