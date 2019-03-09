# coding: utf-8 
import network

ADDRESS=""
PORT=1111

sock=network.newServerSocket()
sock.bind((ADDRESS,PORT))

def communication(thread):
    
    reponse = thread.clientsocket.recv(2048)
    reponse = reponse.decode("utf-8")

    print("message de %s %s" % (thread.ip, thread.port, ))
    print(">>", reponse)
    thread.clientsocket.send("serveur : j'ai bien recu le message".encode())
    
    if reponse=="exit":
        return False
    else:
        return True



continuer = True
while continuer:

    sock.listen(10)
    print( "En écoute...")

    thread = network.newThread(sock.accept())
    thread.start()

    continuer=communication(thread)


    