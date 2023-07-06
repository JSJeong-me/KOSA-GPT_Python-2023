import time
import webbrowser
import pyautogui

# Open a new tab in default browser and navigate to Google
webbrowser.open('http://www.google.com')
time.sleep(3) # wait for the page to load

# Pyautogui commands to type and search
pyautogui.write('current temperature', interval=0.1) # type with a delay in between each keypress
time.sleep(3)
pyautogui.press('enter') # press the 'Enter' key
