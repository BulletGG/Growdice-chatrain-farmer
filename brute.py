from pyautogui import * 
import pyautogui 
import time 
import keyboard 
import random
import win32api, win32con
from os import system



system("title " + "Growdice claimer by @bullet.dev")
print("Growdice claimer made by @bullet.dev")
print(" ")

while 1:
    time.sleep(3)
    location = pyautogui.locateOnScreen('gdicebutton.png', grayscale=True, confidence=0.9)
    if location:
        time.sleep(3)
        print("Joined Chat Rain")
        pyautogui.click(location)
        
    else:
        time.sleep(3)
