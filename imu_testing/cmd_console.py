import socket
import time
import json

COMMAND_SET = {
    'data': 0,
    'status': 1,
    'servo': 2,
    'shutdown': 3
}
SERVER_ADDRESS = '192.168.1.35'
PORT = 5005

def init():
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Over Internet, TCP protocol
    sock.connect((SERVER_ADDRESS, PORT))  # Using .connect() since this is the client
    init_msg = sock.recv(4096).decode('utf-8')
    print("Connection established. Initial message: ", init_msg)

def main():
    while True:
        cmd = input("Pull data (0), send command (1), \"exit\" to exit: ")
        if cmd == "0":
            to_send = "DATA"
            sock.send(to_send.encode('utf-8'))
            print("Request for data sent. Waiting for completion.")
            data = json.loads(sock.recv(4096))
            print("Data received: ", data)
        elif cmd == "1":
            print("Command set: ")
            to_print = ""
            for key, _ in COMMAND_SET.items():
                to_print += key + ", "
            to_print = to_print[:-2]
            print("{", to_print, "} \n")
            while True:
                temp = input("Send what command? (\"back\" to go back)")
                if temp in COMMAND_SET:
                    send_data(temp)
                    break
                elif temp == "back":
                    break
                else:
                    print("Invalid command.")
            print("Command sent. Awaiting execution of command.")
            wait_for_reply()
        elif cmd == "exit":
            sock.close()
            print("Connection terminated, exiting program.")
            break
        else:
            print("Try again.")

def wait_for_reply():
    start = time.time()
    while True:
        msg = sock.recv(4096).decode('utf-8')
        if msg == "DONE":
            print("Status: Done.")
            print("Time elapsed: ", "%.1f" % start-time.time())
            break
        else:
            print("Status: Executing.")
            time.sleep(1)

if __name__ == "__main__":
    init()
    main()
