from findNightServer import findNightServer
from functions import sendMessage, sendScreenshot
from searchViciousBee import searchVicBee
import socket
import threading

altConnection = True
alts = 1

sendMessage("Connected to discord!")

def connectAlt(port):
    hostName = socket.gethostname()
    ipAdress = socket.gethostbyname(hostName)

    print(f"Your ip adress to put in alt: {ipAdress}")

    tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcpsocket.bind((ipAdress, port))

    print("Waiting for alt to connect...")

    sendMessage("Waiting for alt to connect...")

    tcpsocket.listen()
    (client, (ip, port)) = tcpsocket.accept()


    print(f"Alt connected, ip: {ip}, port: {port}")

    sendMessage("Alt connected! Joining servers...")

    return client

def recieveNightServers(client, port):
    while True:
        try:
            url = client.recv(1024)

            url = url.decode()

            open("lastUrl.txt", "w+").write(url)

        except:
            sendMessage("Connection lost with alt.")

            client = connectAlt(port)

            t = threading.Thread(target=recieveNightServers, args=(client, port,))
            t.daemon = True

            t.start()

            break

if altConnection:
    ports = [5555]

    for i in range(alts):
        client = connectAlt(ports[i])

        t = threading.Thread(target=recieveNightServers, args=(client, ports[i],))
        t.daemon = True

        t.start()

while True:
    while True:
        hiveSlot = findNightServer()

        searchVicBee(hiveSlot)
