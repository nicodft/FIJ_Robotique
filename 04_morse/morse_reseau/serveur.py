# coding: utf-8 
import network
<<<<<<< HEAD
import comMorse
=======
>>>>>>> ajout network

ADDRESS=""
PORT=1111

sock=network.newServerSocket()
sock.bind((ADDRESS,PORT))

def communication(thread):
    
<<<<<<< HEAD
    message = thread.clientsocket.recv(4096)
    message = message.decode("utf-8")

    print("message de %s %s" % (thread.ip, thread.port, ))
    print(">>", message)
    message= comMorse.decodeMorse(message)
    print(">>", message)
    thread.clientsocket.send("serveur : j'ai bien recu le message".encode())
    
    if message=="exit":
=======
    reponse = thread.clientsocket.recv(2048)
    reponse = reponse.decode("utf-8")

    print("message de %s %s" % (thread.ip, thread.port, ))
    print(">>", reponse)
    thread.clientsocket.send("serveur : j'ai bien recu le message".encode())
    
    if reponse=="exit":
>>>>>>> ajout network
        return False
    else:
        return True



continuer = True
while continuer:

    sock.listen(10)
<<<<<<< HEAD
    print( "En ecoute...")
=======
    print( "En écoute...")
>>>>>>> ajout network

    thread = network.newThread(sock.accept())
    thread.start()

    continuer=communication(thread)


    