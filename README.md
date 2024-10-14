# Hi, here's how to use my vic hop macro!

### First, you can set your walkspeed in functions.py at line 18, aswell as your discord webhook at line 12 (it is mandatory to set those 2). You can also set the maximum time the macro will wait for the game to load (if it joins a restricted place for example) in findNightServer.py and findNightServerAlt.py at line 125 and 62 respectively.

# How to run the macro
The main computer has to use windows OS for now :/
If you don't run any alt, set altConnection to False in main.py at line 6.
Run main.py first.

# Connecting an alt
Make sure to set altConnection to True in main.py at line 6.
You will need a second device to run an alt, which has to be connected to the same wifi network as the main running computer. It can run on windows, macOS and linux (not tested on linux).
Set your local ip address in alt.py at line 6, you can get it by running main.py with altConnection set as True at line 6.

# Packages to install
You will need to have the following libraries installed with pip:
- fontTools
- pytesseract (watch a tutorial on youtube that tells how to install it, and you'll have to change its path in searchViciousBee.py at line 8 and in findNightServer.py at line 9.
- pynput
- discord
- psutil
- tkinter
- mss
- PIL (pillow)
- pyautogui
