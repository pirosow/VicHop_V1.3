import pytesseract
from pynput.mouse import Button, Controller
import keyboard
import time
from PIL import Image, ImageGrab
import mss
import discord
import psutil
import threading
import tkinter as tk
from datetime import datetime

webHook = "webhook"

mouse = Controller()

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
    tap("esc")

    time.sleep(0.025)

    tap("l")

    time.sleep(0.025)

    tap("enter")


def reset(hive=True):
    press("esc", 0.05)

    time.sleep(0.05)

    press("r", 0.05)

    time.sleep(0.05)

    press("enter", 0.05)

    time.sleep(8)

    if hive:
        screen = screenshot(monitor=claimHiveMonitor)

        text = pytesseract.image_to_string(screen)

        if not "make honey" in text.lower():
            press("w", "d", 3)

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


def tap(k):
    keyboard.press(k)

    time.sleep(0.05)

    keyboard.release(k)


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
