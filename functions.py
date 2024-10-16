import pyautogui
from pynput.mouse import Button, Controller as mouseController
from pynput.keyboard import Controller as keyboardController, Key
import time
from PIL import Image, ImageGrab
import mss
import discord
import psutil
import threading
import tkinter as tk
from datetime import datetime

webHook = "https://discordapp.com/api/webhooks/1274918744975736832/SszQOxEP-syphbG8pXgN9klvLa273CZM0F9JyA4j9BsK8pe390RZ5SMYnfpaPm5--rFJ"

mouse = mouseController()
keyboard = keyboardController()

root = tk.Tk()

walkSpeed = 33.35

screenDims = [root.winfo_screenwidth(), root.winfo_screenheight()]

claimHiveMonitor = {
    "top": 62,
    "left": 852,
    "width": 1136 - 852,
    "height": 121 - 62,
    "mon": 0,
}

def isColorClose(color1, color2, maxDiff):
    for index, col in enumerate(color1):
        if abs(col - color2[index]) <= maxDiff:
            continue

        else:
            return False

    return True


def isWindowOpen(windowName):
    for process in psutil.process_iter(['name']):
        try:
            if process.info['name'] == windowName:
                return True

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return False

def sendMessage(message, picture=None):
    webhook = discord.SyncWebhook.from_url(webHook)

    tm = datetime.now()

    webhook.send(f"[{tm.hour}:{tm.minute}:{tm.second}] {message}") if picture == None else webhook.send(f"[{tm.hour}:{tm.minute}:{tm.second}] {message}", file=picture)


def sendScreenshot(message):
    screen = screenshot()

    screen.save("screenshot.png")

    screen = open("screenshot.png", "rb")

    t = threading.Thread(target=sendMessage, args=(message, discord.File(screen)))
    t.daemon = True

    t.start()

def leave():
    keyboard.tap(Key.esc)

    time.sleep(0.025)

    keyboard.tap("l")

    time.sleep(0.025)

    keyboard.tap(Key.enter)


def reset(hive=True):
    press(Key.esc, 0.05)

    time.sleep(0.05)

    press("r", 0.05)

    time.sleep(0.05)

    press(Key.enter, 0.05)

    time.sleep(8)

    if hive:
        if not findImg("images/make_honey1.png", 0.7) and not findImg("images/make_honey2.png", 0.7):
            press("w", "d", 3)

def findImg(img, confidence):
    try:
        pos = pyautogui.locateCenterOnScreen(img, confidence=confidence)

        pyautogui.moveTo(pos)

        return True

    except:
        return False

def press(*args):
    keys = list(args)
    keys.pop(len(keys) - 1)

    for key in keys:
        keyboard.press(key)

        time.sleep(0.1)

    time.sleep(args[len(args) - 1] * 33.35 / walkSpeed)

    for key in keys:
        keyboard.release(key)

        time.sleep(0.1)


def screenshot(monitor=False):
    with mss.mss() as sct:
        if monitor:
            screen = sct.grab(monitor)

        else:
            screen = sct.grab(sct.monitors[0])

    screen = Image.frombytes("RGB", screen.size, screen.bgra, "raw", "BGRX")

    return screen


def click(pos):
    mouse.position = pos

    time.sleep(0.05)

    mouse.click(Button.left)

    time.sleep(0.05)

def offsetDims(pos, xy):
    if xy == "list":
        return (int(pos[0] * (screenDims[0] / 1920)), int(pos[1] * (screenDims[1] / 1080)))

    elif xy == "x":
        return int(pos * (screenDims[0] / 1920))

    else:
        return int(pos * (screenDims[1] / 1080))
