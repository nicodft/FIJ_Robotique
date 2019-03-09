# coding: utf-8 
import network
<<<<<<< HEAD
import comMorse
=======
>>>>>>> ajout network


ADDRESS=""
PORT=1111

while True:

    sock = network.newClientSocket()
    sock.connect((ADDRESS, PORT))

    print("message a envoyer:")
    message = input(">> ") # utilisez raw_input() pour les anciennes versions python
<<<<<<< HEAD
    morse = comMorse.encodeTexte(message)
    sock.send(morse.encode())

    reponse = sock.recv(4096)
=======
    sock.send(message.encode())

    reponse = sock.recv(9999999)
>>>>>>> ajout network

    print(reponse.decode("utf-8"))
    if message =="exit":
        break

