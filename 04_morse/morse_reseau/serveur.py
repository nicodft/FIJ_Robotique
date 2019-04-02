# coding: utf-8 
import network
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import comMorse
=======
>>>>>>> ajout network
=======
import parPhrase
>>>>>>> ajout matrice3D et finlaisation exos morse
=======
import comMorse
>>>>>>> modif morse et ajout commentaires
=======
import comMorse
>>>>>>> 74d3d7597b00173dec139c1220d5d72e4079561e

ADDRESS=""
PORT=1111

sock=network.newServerSocket()
sock.bind((ADDRESS,PORT))

def communication(thread):
    
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 74d3d7597b00173dec139c1220d5d72e4079561e
    message = thread.clientsocket.recv(4096)
    message = message.decode("utf-8")

    print("message de %s %s" % (thread.ip, thread.port, ))
    print(">>", message)
    message= comMorse.decodeMorse(message)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 74d3d7597b00173dec139c1220d5d72e4079561e
    print(">>", message)
    thread.clientsocket.send("serveur : j'ai bien recu le message".encode())
    
    if message=="exit":
<<<<<<< HEAD
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
=======
>>>>>>> modif morse et ajout commentaires
    print(">>", message)
    thread.clientsocket.send("serveur : j'ai bien recu le message".encode())
    
<<<<<<< HEAD
    if reponse=="exit":
>>>>>>> ajout network
=======
    if message=="exit":
>>>>>>> ajout matrice3D et finlaisation exos morse
=======
>>>>>>> 74d3d7597b00173dec139c1220d5d72e4079561e
        return False
    else:
        return True



continuer = True
while continuer:

    sock.listen(10)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    print( "En ecoute...")
=======
    print( "En écoute...")
>>>>>>> ajout network
=======
    print( "En ecoute...")
>>>>>>> ajout matrice3D et finlaisation exos morse
=======
    print( "En ecoute...")
>>>>>>> 74d3d7597b00173dec139c1220d5d72e4079561e

    thread = network.newThread(sock.accept())
    thread.start()

    continuer=communication(thread)


    