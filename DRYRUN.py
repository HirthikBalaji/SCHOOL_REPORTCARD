from pyautogui import click, locateOnScreen, moveTo
import time
import pyperclip
import os
import csv
import keyboard
import webbrowser as web
# phone_no = "+91XXXXXXXXXX"
# path = "doc.png"


def chk_img(img):
	location = None
	conf = .9
	counter = 0
	while location is None:
		if counter==5:
			print("Setting confidence to .8")
			conf = .8
		elif counter==10:
			print("Setting confidence to .75")
			conf = .75
		location = locateOnScreen(img,confidence=conf)
		counter = counter+1
		time.sleep(1)
	return location

def send(phone_no,path,message=''):
	web.open(f"https://web.whatsapp.com/send?phone={phone_no}")
	time.sleep(3)
	keyboard.press_and_release('f11')
	#time.sleep(4)
	location = chk_img("link2.png")
	print(location,type(location))
	moveTo(location[0] + location[2]/2, location[1] + location[3]/2)
	click()
	#time.sleep(2)
	location = None
#	while location is None:
#		location = locateOnScreen('doc.png',confidence=.85)
	location = chk_img("doc.png")
	print(location,type(location))
	moveTo(location[0] + location[2]/2, location[1] + location[3]/2)
	click()
	time.sleep(2)
	pyperclip.copy(os.path.abspath(path))
	keyboard.press("ctrl")
	keyboard.press("v")
	keyboard.release("v")
	keyboard.release("ctrl")
	time.sleep(.51)
	keyboard.press("enter")
	keyboard.release("enter")
	#time.sleep(6)
	location=None
#	while location is None:
#		location = locateOnScreen('send.png',confidence=.85)
	location = chk_img("send.png")
	print(location,type(location))
	if message != '':
		keyboard.write(message)
	time.sleep(1)
	moveTo(location[0] + location[2]/2, location[1] + location[3]/2)
	click()
	time.sleep(2)
	location=None
	while location is None:
		location = locateOnScreen('done.png',confidence=.8)
#	location = chk_img("done.png")
	print(location,type(location))
	keyboard.press("ctrl")
	keyboard.press("w")
	keyboard.release("w")
	keyboard.release("ctrl")
#send(phone_no,path,"Test_Run")

