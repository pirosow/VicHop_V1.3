import pytesseract
from pynput.mouse import Button, Controller
import time
import pytesseract as tesseract
from randomServer import joinRandomServer
from functions import isWindowOpen, isColorClose, sendMessage, sendScreenshot, leave, reset, press, screenshot, tap, click, offsetDims

tesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

mouse = Controller()

claimHiveMonitor = {
        "top": offsetDims(62, "y"),
        "left": offsetDims(852, "x"),
        "width": offsetDims(1136 - 852, "x"),
        "height": offsetDims(121 - 62, "y"),
        "mon": 0,
}

def waitForLoading(maxWaitTime=20):
    tm = time.time()

    while True:
        screen = screenshot()

        if screen.getpixel((1300, 812)) == (34, 87, 168):
            break

        elif time.time() - tm >= maxWaitTime:
            return False

        time.sleep(0.05)

    tm = time.time()

    while True:
        screen = screenshot()

        if screen.getpixel((1300, 812)) != (34, 87, 168):
            return True

        elif time.time() - tm >= 20:
            return False

        time.sleep(0.05)

def detectNight():
    screen = screenshot()

    if isColorClose(screen.getpixel((1376, 914)), (86, 100, 107), 5):
        sendScreenshot("Night server found :D")

        return True

    return False

def claimHive():
    press("w", "d", 4)

    time.sleep(0.1)

    press("s", 0.5)

    time.sleep(0.1)

    press("a", 0.3)

    claimingHive = True

    while claimingHive:
        hiveSlot = 7

        for loop in range(6):
            hiveSlot -= 1

            time.sleep(0.5)

            text = pytesseract.image_to_string(screenshot(monitor=claimHiveMonitor))

            print(text)

            if "claim" in text.lower() and "hive" in text.lower():
                press("e", 0.5)

                sendScreenshot(f"Claimed hive slot {hiveSlot}")

                return hiveSlot

            elif loop == 5:
                break

            else:
                press("a", 1.1)

        reset(hive=False)

        press("w", "d", 4)

        time.sleep(0.025)

        press("s", 0.5)

        time.sleep(0.025)

        press("a", 0.3)

def findNightServer(claim=True):
    hiveSlot = 0

    serverLoop = 0

    while True:
        serverLoop += 1

        if isWindowOpen("RobloxPlayerBeta.exe"):
            leave()

        joinRandomServer(1537690962)

        sendMessage(f"Joining server x{serverLoop}")

        if not waitForLoading(maxWaitTime=10):
            sendMessage("Closing roblox experience is restricted error")

            continue

        time.sleep(0.5)

        if not detectNight():
            continue

        click((1000, 1000))

        time.sleep(0.5)

        if claim:
            hiveSlot = claimHive()

            time.sleep(0.5)

        break

    if claim:
        return hiveSlot