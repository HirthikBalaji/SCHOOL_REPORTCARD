import os

import PyPDF2
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
import io
import shutil


def add_signature(input_path, principal_image_path='static/signature_PRINCIPAL.jpg',
                  ct_image_path="static/Sign_ct.jpg"):
    # Load the input PDF file
    # input_path = '173-12.pdf'
    output_path = f'{input_path.split(".")[0]}_Signed_fully.pdf'
    # input_path = f'{input_path.split(".")[0]}_signed.pdf'
    # image_path = 'static/signature.jpg'
    y = 230
    x = 35
    width = 80
    height = 18
    y_ct = 230
    x_ct = 250
    width_ct = 80
    height_ct = 18
    with open(input_path, 'rb') as input_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(input_file)

        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfWriter()

        # Get the first page of the PDF document
        page = pdf_reader.pages[0]

        # Open the image file and create an ImageReader object
        with open(principal_image_path, 'rb') as image_file:
            image_reader = ImageReader(image_file)
        with open(ct_image_path, 'rb') as image_file2:
            image_reader2 = ImageReader(image_file2)

        # Create a canvas object and add the image to it
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.drawImage(image_reader, x, y, width, height)
        can.drawImage(image_reader2, x_ct, y_ct, width_ct, height_ct)
        can.save()
        # Add the image to the page
        page.merge_page(PyPDF2.PdfReader(packet).pages[0])
        pdf_writer.add_page(page)

        # Save the updated PDF file
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)
    # time.sleep(0.5)
    os.remove(input_path)


def encrypt(file):
    # Open the PDF file
    with open(file, 'rb') as pdf_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        # for i in range(0, len(pdf_reader.pages)):
        # Get the first page of the PDF document
        page = pdf_reader.pages[0]
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(page)
        print(f'{file.split("/")[1].split("_")[0]}')
        pdf_writer.encrypt(user_password=f'{file.split("/")[1].split("_")[0]}', owner_pwd=':^\":K<x<hClzlu\':',
                           use_128bit=True,
                           permissions_flag=0)
        with open(f'EXTRACT/{file.split("/")[1].split("_")[0]}.pdf', 'wb') as output_file:
            pdf_writer.write(output_file)
    os.remove(file)


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
            # pdf_writer.encrypt(user_password='password', owner_pwd='None',
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
                        if not os.path.exists("EXTRACT"):
                            os.mkdir("EXTRACT")
                        shutil.move(f"{adm}.pdf", f"./EXTRACT/{adm}.pdf")
                    else:
                        raise ValueError(f"NO ADMISSION NUMBER FOUND IN PAGE {i + 1} in {file}")


def read(file):
    # TBD
    pass
