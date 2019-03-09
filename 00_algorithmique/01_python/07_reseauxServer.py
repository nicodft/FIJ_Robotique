# coding: utf-8 

import socket
import threading

ADDRESS=""
PORT=1111

class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))

    def run(self): 

        print("Connexion de %s %s" % (self.ip, self.port, ))

        reponse = self.clientsocket.recv(2048)
        reponse= reponse.decode("utf-8")
        print("message recu : ", reponse)
        self.clientsocket.send(("j'ai recu le message : "+ reponse).encode())

        print("Client déconnecté...")

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((ADDRESS,PORT))

while True:
    tcpsock.listen(10)
    print( "En écoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()