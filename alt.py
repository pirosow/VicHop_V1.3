from findNightServerAlt import findNightServer
import socket
from fontTools.misc.textTools import tobytes

hostName = socket.gethostname()
ipAdress = "192.168.0.172" #my local ip xd

tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 5555

tcpsocket.connect((ipAdress, port))

while True:
    url = findNightServer(claim=False)

    url = tobytes(url)

    tcpsocket.send(url)