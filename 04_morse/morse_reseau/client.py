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

while True:

    sock = network.newClientSocket()
    sock.connect((ADDRESS, PORT))

    print("message a envoyer:")
    message = input(">> ") # utilisez raw_input() pour les anciennes versions python
<<<<<<< HEAD
<<<<<<< HEAD
    morse = comMorse.encodeTexte(message)
    sock.send(morse.encode())

    reponse = sock.recv(4096)
=======
    sock.send(message.encode())
=======
    morse = parPhrase.texte(message)
    sock.send(morse.encode())
>>>>>>> ajout matrice3D et finlaisation exos morse

<<<<<<< HEAD
    reponse = sock.recv(9999999)
>>>>>>> ajout network
=======
    reponse = sock.recv(4096)
>>>>>>> modif et test reseau

    print(reponse.decode("utf-8"))
    if message =="exit":
        break

