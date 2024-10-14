import keyboard
from findNightServer import findNightServer
from searchViciousBee import searchVicBee

while True:
    while not keyboard.is_pressed("b"):
        pass

    while True:
        hiveSlot = findNightServer()

        searchVicBee(hiveSlot)