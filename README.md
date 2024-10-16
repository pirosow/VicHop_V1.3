# Hi, here's how to use my vic hop macro!

### First, you can set your walkspeed in functions.py at line 18, aswell as your discord webhook at line 12 (it is mandatory to set those 2). You can also set the maximum time the macro will wait for the game to load (if it joins a restricted place for example) in findNightServer.py and findNightServerAlt.py at line 125 and 62 respectively.

# How to run the macro
The main computer has to use windows OS for now :/
If you don't run any alt, set altConnection to False in main.py at line 6.
Run main.py first.

# Connecting an alt
Make sure to set altConnection to True in main.py at line 7.
Set alts to the number of alts you'll connect in main.py at line 8.
You will need other devices to run a alts, which have to be connected to the same wifi network as the main running computer. They can run on windows, macOS and linux (not tested on linux).
You'll have to set the port on every alt device in alt.py at line 11, and change the numbers in main.py at line 58 to the corresponding ports.
Set your local ip address in alt.py at line 6, you can get it by running main.py with altConnection set as True at line 6.
Run the alts in the same order as the ports in main.py at line 58.

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
