#!/usr/bin/python3
import pyautogui
import time

message = input("What message do you want to keep sending? (Leave this blank if you want to paste your clipboard)  ")
repeat = int(input("How many times do you want to send the message?  "))
ready = input("Press Enter when your messaging app is loaded up.")

print("You have five seconds to refocus the text input area of your messaging app")
#Wait for focus the text input area
time.sleep(5)

for i in range(0,repeat):         #Message sending loop
	if message != "":
		pyautogui.typewrite(message)     
		pyautogui.press("enter")
		pyautogui.hotkey('ctrl', 'v')
		pyautogui.press("enter")
	else:
		pyautogui.hotkey('ctrl', 'v')      
		pyautogui.press("enter")

print("Done\n")