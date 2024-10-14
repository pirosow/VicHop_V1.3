from findNightServer import findNightServer
from searchViciousBee import searchVicBee
import socket
import threading

altConnection = True

def connectAlt():
    hostName = socket.gethostname()
    ipAdress = socket.gethostbyname(hostName)

    print(f"Your ip adress to put in alt: {ipAdress}")

    port = 5555

    tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcpsocket.bind((ipAdress, port))

    print("Waiting for alt to connect...")

    tcpsocket.listen()
    (client, (ip, port)) = tcpsocket.accept()


    print(f"Alt connected, ip: {ip}, port: {port}")

    return client

def recieveNightServers(client):
    while True:
        url = client.recv(1024)

        url = url.decode()

        open("lastUrl.txt", "w+").write(url)

if altConnection:
    client = connectAlt()

    t = threading.Thread(target=recieveNightServers, args=(client,))
    t.daemon = True

    t.start()

while True:
    while True:
        hiveSlot = findNightServer()

        searchVicBee(hiveSlot)