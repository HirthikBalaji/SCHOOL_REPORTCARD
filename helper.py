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
import glob
import PyWhatKit.pywhatkit as pwk
import PyPDF2
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
import io


def add_principal_sign(input_path,image_path='static/signature_PRINCIPAL.jpg'):
    # Load the input PDF file
    #input_path = '173-12.pdf'
    output_path = f'{input_path.split(".")[0]}_Signed_fully.pdf'
    input_path = f'{input_path.split(".")[0]}_signed.pdf'
    # image_path = 'static/signature.jpg'
    y = 230
    x = 35
    width = 80
    height = 18
    with open(input_path, 'rb') as input_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(input_file)

        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfWriter()

        # Get the first page of the PDF document
        page = pdf_reader.pages[0]

        # Open the image file and create an ImageReader object
        with open(image_path, 'rb') as image_file:
            image_reader = ImageReader(image_file)

        # Create a canvas object and add the image to it
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.drawImage(image_reader, x, y, width, height)
        can.save()

        # Add the image to the page
        page.merge_page(PyPDF2.PdfReader(packet).pages[0])
        pdf_writer.add_page(page)

        # Save the updated PDF file
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)


def add_class_teacher_sign(input_path,image_path='static/signature_CLASS_TEACHER.jpg'):
    # Load the input PDF file
    #input_path = '173-12.pdf'
    output_path = f'{input_path.split(".")[0]}_signed.pdf'
    #image_path = 'static/signature.jpg'
    y = 230
    x = 250
    width = 80
    height = 18
    with open(input_path, 'rb') as input_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(input_file)

        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfWriter()

        # Get the first page of the PDF document
        page = pdf_reader.pages[0]

        # Open the image file and create an ImageReader object
        with open(image_path, 'rb') as image_file:
            image_reader = ImageReader(image_file)

        # Create a canvas object and add the image to it
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.drawImage(image_reader, x, y, width, height)
        can.save()

        # Add the image to the page
        page.merge_page(PyPDF2.PdfReader(packet).pages[0])
        pdf_writer.add_page(page)

        # Save the updated PDF file
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)


def encrypt(file):
    # Open the PDF file
    with open(file, 'rb') as pdf_file:

        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        #for i in range(0, len(pdf_reader.pages)):
        # Get the first page of the PDF document
        page = pdf_reader.pages[0]
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(page)
        pdf_writer.encrypt(user_password='password', owner_pwd='None',
                           use_128bit=True,
                           permissions_flag=0)
        with open(f'{file.split("_S")[0]}_ENCRYPTED.pdf', 'wb') as output_file:
            pdf_writer.write(output_file)

def extract_pages(file):
    # Open the PDF file
    with open(file, 'rb') as pdf_file:

        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for i in range(0, len(pdf_reader.pages)):
            # Get the first page of the PDF document
            page = pdf_reader.pages[i]
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(page)
            #pdf_writer.encrypt(user_password='password', owner_pwd='None',
            #                   use_128bit=True,
            #                   permissions_flag=0)
            # Extract the text from the page
            text = page.extract_text()
            # Print the extracted text
            li = text.replace(' ', '').split()
            for j in li:
                if 'admission' in j.lower():
                    adm = j.split(":")[1]
                    if adm != "":
                        with open(f'{adm}.pdf', 'wb') as output_file:
                            pdf_writer.write(output_file)
                    else:
                        raise ValueError(f"NO ADMISSION NUMBER FOUND IN PAGE {i+1} in {file}")

