from socket import *
from threading import *
from tkinter import *

CSocket = socket(AF_INET, SOCK_STREAM)
CSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

IP = "127.0.0.1"
port = 8080
CSocket.connect((IP, port))

UI = Tk()
UI.title("Connect to: "+ IP+ ":"+str(port))

msg = Text(UI, width=40)
msg.grid(row=0, column=0, padx=20, pady=20)

input = Entry(UI, width=50)
input.insert(0, "")
input.grid(row=1, column=0, padx=10, pady=10)

def sending():
    Cmsg = input.get()
    msg.insert(END, "\n" + "User: "+ Cmsg)
    CSocket.send(Cmsg.encode("utf-8"))

send = Button(UI, text="Send", width=10, command=sending)
send.grid(row=1, column=1, padx=5, pady=5)

def receive():
    while True:
        Smsg = CSocket.recv(1024).decode("utf-8")
        print(Smsg)
        msg.insert(END, "\n"+Smsg)

receiving = Thread(target=receive)
receiving.daemon = True
receiving.start()
UI.mainloop()
