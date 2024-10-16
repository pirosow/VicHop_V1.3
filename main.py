from findNightServer import findNightServer
from functions import sendMessage, sendScreenshot
from searchViciousBee import searchVicBee
import socket
import threading
import time

altConnection = True

timeout = 20 * 60 #max time the macro will wait before stopping connection & try to reconnect

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
    lastCheck = time.time()

    while True:
        try:
            url = client.recv(1024)

            if not url:
                if time.time() - lastCheck >= timeout:
                    raise TimeoutError

            else:
                lastCheck = time.time()

            url = url.decode()

            open("lastUrl.txt", "w+").write(url)

        except Exception as e:
            print(e)

            print("Lost connection to alt. Closing socket client...")

            sendMessage("Lost connection to alt. Closing socket client...")

            client.shutdown(socket.SHUT_RDWR)

            client.close()

            time.sleep(5)

            print("Reconnecting to alt...")

            client = connectAlt(port)

            t = threading.Thread(target=recieveNightServers, args=(client, port,))
            t.daemon = True

            t.start()

            break

if altConnection:
    ports = [5555]

    for port in ports:
        client = connectAlt(port)

        t = threading.Thread(target=recieveNightServers, args=(client, port,))
        t.daemon = True

        t.start()

while True:
    while True:
        hiveSlot = findNightServer()

        searchVicBee(hiveSlot)