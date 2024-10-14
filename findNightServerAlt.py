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

        if isColorClose(screen.getpixel(offsetDims((1300, 812), "list")), (35, 79, 171), 5):
            break

        elif time.time() - tm >= maxWaitTime:
            return False

        time.sleep(0.05)

    tm = time.time()

    while True:
        screen = screenshot()

        if not isColorClose(screen.getpixel(offsetDims((1300, 812), "list")), (35, 79, 171), 5):
            return True

        elif time.time() - tm >= maxWaitTime:
            return False

        time.sleep(0.05)

def detectNight():
    screen = screenshot()

    if isColorClose(screen.getpixel(offsetDims((1376, 914), "list")), (86, 100, 107), 5):
        return True

    return False

def findNightServer(claim=True):
    hiveSlot = 0

    serverLoop = 0

    while True:
        serverLoop += 1

        url = joinRandomServer(1537690962)

        if not waitForLoading(maxWaitTime=45):
            continue

        time.sleep(2)

        if not detectNight():
            continue

        sendScreenshot(f"Night server found on alt :D (attempts: {serverLoop})")

        click(offsetDims((1000, 1000), "list"))

        time.sleep(0.5)

        break

    return url