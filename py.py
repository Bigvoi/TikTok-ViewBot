import pyautogui
import time
import os
import requests
import pyperclip
import pyautogui

lien = input("https://vm.tiktok.com/ZMLbPGt9p/ : ")

for i in range (2689001):

    os.system("start tiktok")
    time.sleep(1)
    pyperclip.copy(f"{lien}")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(300)
    os.system("taskkill /IM tiktok.exe")
