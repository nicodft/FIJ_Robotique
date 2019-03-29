# coding: utf-8 
import network
import parPhrase


ADDRESS=""
PORT=1111

while True:

    sock = network.newClientSocket()
    sock.connect((ADDRESS, PORT))

    print("message a envoyer:")
    message = input(">> ") # utilisez raw_input() pour les anciennes versions python
    morse = parPhrase.texte(message)
    sock.send(morse.encode())

    reponse = sock.recv(4096)

    print(reponse.decode("utf-8"))
    if message =="exit":
        break

