import pytesseract
from pynput.mouse import Button, Controller
import keyboard
import time
import pytesseract as tesseract
from functions import isWindowOpen, isColorClose, sendMessage, sendScreenshot, leave, reset, press, screenshot, tap, click, offsetDims

tesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

mouse = Controller()

hiveSlot = 7

chatMonitor = {
    "top": offsetDims(62, "y"),
    "left": offsetDims(1342, "x"),
    "width": offsetDims(1919 - 852, "x"),
    "height": offsetDims(282 - 62, "y"),
    "mon": 0,
}

claimHiveMonitor = {
        "top": offsetDims(62, "y"),
        "left": offsetDims(852, "x"),
        "width": offsetDims(1136 - 852, "x"),
        "height": offsetDims(121 - 62, "y"),
        "mon": 0,
}

def cannon(rst=True):
    loop = 0

    while True:
        if rst or loop > 0:
            reset()

        time.sleep(0.05)

        press("w", 0.75)

        press("d", 1.1 * (7 - hiveSlot))

        keyboard.press("d")

        press(" ", 0.05)

        time.sleep(1.2)

        keyboard.release("d")

        screen = screenshot(monitor=claimHiveMonitor)

        text = pytesseract.image_to_string(screen)

        if "fire" in text.lower():
            break

        loop += 1

def goToPepper():
    cannon(rst=False)

    press("d", 2)

    keyboard.press("d")

    press(" ", 0.05)

    time.sleep(1.4)

    keyboard.release("d")

    time.sleep(0.05)

    keyboard.press("w")

    press(" ", 0.05)

    time.sleep(2)

    for _ in range(3):
        press(" ", 0.05)

        time.sleep(0.7)

    time.sleep(1)

    press(" ", 0.05)

    time.sleep(0.5)

    keyboard.release("w")

    time.sleep(0.05)

    press("w", "d", 2)

    press(" ", 0.05)

    press("d", 2.5)

    press("s", 0.5)

    keyboard.press("d")

    time.sleep(0.1)

    press(" ", 0.05)

    time.sleep(0.5)

    keyboard.release("d")

def goToRose():
    cannon()

    press("e", 0.05)

    time.sleep(0.05)

    for _ in range(2):
        press(" ", 0.05)

        time.sleep(0.1)

    press("d", 3)

    press(" ", 0.05)

    time.sleep(1)

    press("a", 2)

    press("s", 0.5)

    press("d", 0.5)

def goToMtn():
    cannon()

    press("e", 0.05)

    time.sleep(3.5)

    press("w", 1.5)

    press("a", 1)

def goToCac():
    cannon()

    press("e", 0.05)

    time.sleep(0.85)

    for _ in range(2):
        press(" ", 0.05)

        time.sleep(0.1)

    press("d", 2.5)

    press(" ", 0.05)

    time.sleep(1)

    press("a", 2)

def vicBeeAttack():
    sendScreenshot("Vic bee found, attacking!")

    tm = time.time()

    while time.time() - tm < 60:
        for _ in range(2):
            press("w", 0.5)

            press("d", 0.5)

            press("s", 0.5)

            press("a", 0.5)

        press("/", 0.05)

        press("enter", 0.05)

        screen = screenshot(monitor=chatMonitor)

        text = pytesseract.image_to_string(screen)

        if "defeated" in text.lower():
            break

def searchVicBeePepper():
    press("d", 2)

    press("w", 0.7)

    press("a", 2)

    press("w", 0.7)

    press("d", 2)

    press("/", 0.05)

    press("enter", 0.05)

    screen = screenshot(monitor=chatMonitor)

    text = pytesseract.image_to_string(screen)

    if "vicious bee is attacking" in text.lower():
        press("a", "s", 0.5)

        vicBeeAttack()

        return True

    return False

def searchVicBeeRose():
    press("w", 2)

    press("d", 0.7)

    press("s", 2)

    press("d", 0.7)

    press("w", 2)

    press("d", 0.7)

    press("s", 2)

    press("/", 0.05)

    press("enter", 0.05)

    screen = screenshot(monitor=chatMonitor)

    text = pytesseract.image_to_string(screen)

    if "vicious bee is attacking" in text.lower():
        press("w", "a", 0.5)

        vicBeeAttack()

        return True

    return False

def searchVicBeeMtn():
    press("s", 2)

    press("d", 0.7)

    press("w", 2)

    press("d", 0.7)

    press("s", 2)

    press("d", 0.7)

    press("w", 2)

    press("/", 0.05)

    press("enter", 0.05)

    screen = screenshot(monitor=chatMonitor)

    text = pytesseract.image_to_string(screen)

    if "vicious bee is attacking" in text.lower():
        press("s", "a", 0.5)

        vicBeeAttack()

        return True

    return False

def searchVicBeeCac():
    press("d", 3.5)

    press("s", 0.7)

    press("a", 3.5)

    press("d", 0.5)

    press("/", 0.05)

    press("enter", 0.05)

    screen = screenshot(monitor=chatMonitor)

    text = pytesseract.image_to_string(screen)

    if "vicious bee is attacking" in text.lower():
        vicBeeAttack()

        return True

    return False

def searchVicBee(hiveSlotParam):
    global hiveSlot

    hiveSlot = hiveSlotParam

    goToPepper()

    found = searchVicBeePepper()

    if found:
        return

    goToRose()

    found = searchVicBeeRose()

    if found:
        return

    goToMtn()

    found = searchVicBeeMtn()

    if found:
        return

    goToCac()

    searchVicBeeCac()

    if not found:
        sendScreenshot("No vicious bee found :/")