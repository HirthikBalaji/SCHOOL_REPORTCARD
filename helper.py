from pyautogui import click, hotkey, locateOnScreen, moveTo, press, size, typewrite
import time
import pyperclip
import os
import keyboard
import webbrowser as web
# phone_no = "+91XXXXXXXXXX"
# path = "173-12_ENCRYPTED.pdf"
def send(phone_no,path):
	web.open(f"https://web.whatsapp.com/send?phone={phone_no}")
	time.sleep(3)
	keyboard.press_and_release('f11')
	#time.sleep(4)
	location = None
	while location is None:
		location = locateOnScreen('link2.png',confidence=.6)
	print(location,type(location))
	moveTo(location[0] + location[2]/2, location[1] + location[3]/2)
	click()
	#time.sleep(2)
	location = None
	while location is None:
		location = locateOnScreen('doc.png',confidence=.7)
	print(location,type(location))
	moveTo(location[0] + location[2]/2, location[1] + location[3]/2)
	click()
	time.sleep(3)
	pyperclip.copy(os.path.abspath(path))
	keyboard.press("ctrl")
	keyboard.press("v")
	keyboard.release("v")
	keyboard.release("ctrl")
	time.sleep(1)
	keyboard.press("enter")
	keyboard.release("enter")
	#time.sleep(6)
	location=None
	while location is None:
		location = locateOnScreen('send.png',confidence=.7)
	print(location,type(location))
	moveTo(location[0] + location[2]/2, location[1] + location[3]/2)
	click()
	time.sleep(2)
	keyboard.press("ctrl")
	keyboard.press("w")
	keyboard.release("w")
	keyboard.release("ctrl")
# send(phone_no,path)
