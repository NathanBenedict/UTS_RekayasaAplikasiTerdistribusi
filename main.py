from socket import *
from threading import *

HSocket = socket(AF_INET, SOCK_STREAM)
HSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)

IP = "127.0.0.1"
port = 7500
HSocket.bind((IP, port))
HSocket.listen()
print ("Connecting...")

clients = set()
def clientThread(CSocket, CAddress):
    while True:
        message = CSocket.recv(1024).decode("utf-8")
        print(CAddress[0] + ":" + str(CAddress[1]) +" says: "+ message)
        for client in clients:
            if client is not CSocket:
                client.send((CAddress[0] + ":" + str(CAddress[1]) +" says: "+ message).encode("utf-8"))

        if not message:
            clients.remove(CSocket)
            print(CAddress[0] + ":" + str(CAddress[1]) +" disconnected")
            break

    CSocket.close()

while True:
    CSocket, CAddress = HSocket.accept()
    clients.add(CSocket)
    print ("Connected to: ", CAddress[0] + ":" + str(CAddress[1]))
    thread = Thread(target=clientThread, args=(CSocket, CAddress, ))
    thread.start()