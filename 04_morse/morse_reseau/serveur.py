# coding: utf-8 
import network
<<<<<<< HEAD
<<<<<<< HEAD
import comMorse
=======
>>>>>>> ajout network
=======
import parPhrase
>>>>>>> ajout matrice3D et finlaisation exos morse

ADDRESS=""
PORT=1111

sock=network.newServerSocket()
sock.bind((ADDRESS,PORT))

def communication(thread):
    
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
    reponse = thread.clientsocket.recv(4096)
>>>>>>> modif et test reseau
    reponse = reponse.decode("utf-8")
=======
    message = thread.clientsocket.recv(4096)
    message = message.decode("utf-8")
>>>>>>> ajout matrice3D et finlaisation exos morse

    print("message de %s %s" % (thread.ip, thread.port, ))
    print(">>", message)
    message= parPhrase.morse(message)
    print(">>", message)
    thread.clientsocket.send("serveur : j'ai bien recu le message".encode())
    
<<<<<<< HEAD
    if reponse=="exit":
>>>>>>> ajout network
=======
    if message=="exit":
>>>>>>> ajout matrice3D et finlaisation exos morse
        return False
    else:
        return True



continuer = True
while continuer:

    sock.listen(10)
<<<<<<< HEAD
<<<<<<< HEAD
    print( "En ecoute...")
=======
    print( "En écoute...")
>>>>>>> ajout network
=======
    print( "En ecoute...")
>>>>>>> ajout matrice3D et finlaisation exos morse

    thread = network.newThread(sock.accept())
    thread.start()

    continuer=communication(thread)


    