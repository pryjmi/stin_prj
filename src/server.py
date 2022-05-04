import socket
import threading
import time as t
from chat_server import *

HEADER = 64
PORT = 5050
SERVER = "0.0.0.0"
ADDR = (SERVER, PORT)
FORMAT = "utf8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle(conn, addr):
    print(f"[NEW CONNECTION {addr} connected.")
    connected = True
    while connected:
        if msg_length := conn.recv(HEADER).decode(FORMAT):
              msg_length = int(msg_length)
              msg = conn.recv(msg_length).decode(FORMAT)
              if msg == DISCONNECT_MESSAGE:
                    connected = False
              else:
                  msg = str(answer(str2list(rem_sym(msg))))
              msg = msg.replace("', ", "\n")
              msg = msg.replace("['", "")
              msg = msg.replace("']", "")
              msg = msg.replace("\n'", "\n")
              msg = msg.replace("\\n", "\n")
              msg = msg.replace('["', "")
              msg = msg.replace('."]', "")

              print(f"[{addr}] {msg}")
              t.sleep(1)
              conn.send(msg.encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")
start()
