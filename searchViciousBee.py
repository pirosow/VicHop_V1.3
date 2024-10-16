from pynput.mouse import Button, Controller as mouseController
from pynput.keyboard import Controller as keyboardController, Key
import time
from functions import isWindowOpen, isColorClose, sendMessage, sendScreenshot, leave, reset, press, screenshot, click, offsetDims, keyboard, findImg

mouse = mouseController()
keyboard = keyboardController()

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

time.sleep(2)

def cannon(rst=True):
    loop = 0

    while True:
        if loop >= 20:
            break

        if rst or loop > 0:
            reset()

        time.sleep(0.05)

        press("w", 0.75)

        press("d", 1.1 * (7 - hiveSlot))

        keyboard.press("d")

        press(" ", 0.05)

        time.sleep(1.2)

        keyboard.release("d")

        time.sleep(0.5)

        if findImg("images/cannon.png", 0.7):
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
            press("w", 1)

            press("d", 1)

            press("s", 1)

            press("a", 1)

        time.sleep(0.1)

        keyboard.tap("/")

        time.sleep(0.05)

        keyboard.tap(Key.enter)

        time.sleep(0.5)


        if findImg("images/defeated.png", confidence=0.7):
            break

def searchVicBeePepper():
    press("d", 2)

    press("w", 0.7)

    press("a", 2)

    press("w", 0.7)

    press("d", 2)

    time.sleep(0.1)

    keyboard.tap("/")

    time.sleep(0.05)

    keyboard.tap(Key.enter)

    time.sleep(0.5)

    if findImg("images/attacking.png", confidence=0.6):
        press("a", "s", 1)

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

    time.sleep(0.1)

    keyboard.tap("/")

    time.sleep(0.05)

    keyboard.tap(Key.enter)

    time.sleep(0.5)

    if findImg("images/attacking.png", confidence=0.6):
        press("w", "a", 1)

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

    time.sleep(0.1)

    keyboard.tap("/")

    time.sleep(0.05)

    keyboard.tap(Key.enter)

    time.sleep(0.5)

    if findImg("images/attacking.png", confidence=0.6):
        press("s", "a", 1)

        vicBeeAttack()

        return True

    return False

def searchVicBeeCac():
    press("d", 3.5)

    press("s", 0.7)

    press("a", 3.5)

    press("d", 0.5)

    time.sleep(0.1)

    keyboard.tap("/")

    time.sleep(0.05)

    keyboard.tap(Key.enter)

    time.sleep(0.5)

    if findImg("images/attacking.png", confidence=0.6):
        for _ in range(2):
            press(".", 0.1)

            time.sleep(0.1)

        vicBeeAttack()

        return True

    return False

def searchVicBee(hiveSlotParam):
    global hiveSlot

    hiveSlot = hiveSlotParam

    sendMessage("Going to pepper")

    goToPepper()

    found = searchVicBeePepper()

    if found:
        sendScreenshot("Vicious bee defeated!")

        return

    sendMessage("No vicious bee found, going to rose")

    goToRose()

    found = searchVicBeeRose()

    if found:
        sendScreenshot("Vicious bee defeated!")

        return

    sendMessage("No vicious bee found, going to mountain")

    goToMtn()

    found = searchVicBeeMtn()

    if found:
        sendScreenshot("Vicious bee defeated!")

        return

    sendMessage("No vicious bee found, going to cactus")

    goToCac()

    searchVicBeeCac()

    if not found:
        sendScreenshot("No vicious bee found :/")

    else:
        sendScreenshot("Vicious bee defeated!")