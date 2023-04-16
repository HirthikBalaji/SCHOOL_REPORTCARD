import glob
from whatsapp_document_sender import send
from helper import add_signature, encrypt, extract_pages,read


extract_pages("REPORTCARD.pdf")
list1 = glob.glob("EXTRACT/*.pdf")
for i in list1:
    add_signature(i, principal_image_path='signature.jpg', ct_image_path="signature.jpg")
list2 = glob.glob("EXTRACT/*.pdf")
for i in list2:
    encrypt(i)
for i in read("REPORT.csv"):
    message = f"Dear Parent,\n greetings from Adhyapana, hereby we have attached the Report card of your " \
              f"ward\nPassword is:{i['admno']}"
    send(i["phno"],f"EXTRACT/{i['admno']}.pdf",message=message)
