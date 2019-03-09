import socket

ADDRESS=""
PORT=1111

coninuer= True
while coninuer:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ADDRESS, PORT))

    print("Le nom du fichier que vous voulez récupérer:")
    file_name = input(">> ") # utilisez raw_input() pour les anciennes versions python
    s.send(file_name.encode())

    reponse = s.recv(9999999)

    print(reponse.decode("utf-8"))