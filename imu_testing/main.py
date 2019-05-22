import time
import threading
import socket
import json

from smbus2 import SMBusWrapper

SLAVE_ADDRESS = 0x04
SERVER_ADDRESS = '192.168.1.154'  # '192.168.1.35'
PORT = 5000
COMMAND_SET = {
    'data': 0,
    'status': 1,
    'servo': 2,
    'disconnect': 3
}
begin_startup = 0

def init():
    global sock, conn, addr
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((SERVER_ADDRESS, PORT))
    sock.listen()
    conn, addr = sock.accept()

def main():
    global start, command
    start = threading.Thread(target=startup, daemon=False)
    command = threading.Thread(target=command_ingest, daemon=False)
    start.start()
    command.start()

def startup():
    # Pull first batch of IMU data, move servo 360 degrees
    global imu_data, begin_startup
    imu_data = {
        'euler_x': 25.2311, # [0]
        'euler_y': 1.0293,  # [1]
        'euler_z': 0.9203,  # [2]
        'acc_x': 2.3462,    # [3]
        'acc_y': 0.2123,    # [4]
        'acc_z': 1.1909,    # [5]
        'omega_x': 0.0223,  # [6]
        'omega_y': 1.5577,  # [7]
        'omega_z': 1.0091,  # [8]
        'temp': 298.0212    # [9]
    }
    print("Delaying for 5 seconds.")
    time.sleep(5)
    begin_startup = 1

def command_ingest():
    global begin_startup
    while begin_startup == 0:
        print("Arduino relay not ready.")
        time.sleep(1)
    init_msg = "READY"
    conn.send(init_msg.encode('utf-8'))
    print(init_msg)
    while True:
        cmd = json.loads(conn.recv(4096))
        if cmd['CMD'] == "data":
            print("Sending IMU data.")
            time.sleep(1)
            conn.send(json.dumps(imu_data).encode('utf-8'))
            # confirmation = "DONE"
            # conn.send(confirmation.encode('utf-8'))
        elif cmd['CMD'] == "servo":
            if cmd['ARGS'][0] == 0:
                print("Setting position of servo_x to", cmd['ARGS'][1], "degrees.")
            else:
                print("Setting position of servo_y to", cmd['ARGS'][1], "degrees.")
            time.sleep(5)
            confirmation = "DONE"
            conn.send(confirmation.encode('utf-8'))
            print(confirmation)
        elif cmd['CMD'] == "status":
            print("Relaying status.")
            time.sleep(3)
            confirmation = "DONE"
            conn.send(confirmation.encode('utf-8'))
            # print(confirmation)
        elif cmd['CMD'] == "disconnect":
            print("Disconnecting.")
            shutdown = "SHUTDOWN"
            conn.send(shutdown.encode('utf-8'))
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
            print("Connection terminated.")
            break
        else:
            print("Command invalid.")

# TODO: Change command sent over i2c to Arduino to a String format.
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
