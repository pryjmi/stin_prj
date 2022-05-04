import tkinter as tk
import socket

HEADER = 64
PORT = 5050
FORMAT = "utf8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "51.124.243.44"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

window = tk.Tk()
window.geometry("500x500")
window.config(bg="#EAEAEA")
window.title("Chat Bot")

msg = tk.StringVar()
msgbox = tk.Entry(window, textvariable=msg, width=39)
msgbox.place(x=30, y=430)

lstbx = tk.Listbox(window, height=22, width=48, yscroll= rue)
lstbx.place(x=31, y=40)

def send_msg():
    msg = msgbox.get()
    lstbx.insert(tk.END, '(You)')
    lstbx.insert(tk.END, msg)
    lstbx.insert(tk.END, '')
    msgbox.delete(0, 'end')
    send(msg)
    recv()
    lstbx.see('end')
    return msg

def recv():
    received = receive()
    lstbx.insert(tk.END, "(Bot)")
    receivedlist = received.split("\n")
    for r in receivedlist:
      lstbx.insert(tk.END, r)
    lstbx.insert(tk.END, "")
  
send_btn = tk.Button(window, text="Send", bg="grey", fg="black", command=send_msg)
send_btn.place(x=400, y=429)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def receive():
    return client.recv(1024).decode(FORMAT)

window.mainloop()
