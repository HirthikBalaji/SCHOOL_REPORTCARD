
# WhatsApp Document Sender
This is a Python script that uses the PyAutoGUI library to automate the sending of a document on WhatsApp Web. The script can be used to send a document to a specific phone number with an optional message.

## Requirements
The script requires the following Python packages to be installed:

PyAutoGUI
pyperclip
keyboard
webbrowser

The script also requires that the user has WhatsApp Web open and logged in on their web browser.

## Usage
To use the script, simply call the send() function with the following parameters:

phone_no: the phone number of the recipient, in international format (e.g., "+91XXXXXXXXXX")
path: the file path of the document to be sent
message (optional): a message to be sent along with the document

For example:
```python
from whatsapp_document_sender import send

phone_no = "+919876543210"
path = "/path/to/document.pdf"
message = "Here's the document you requested."

send(phone_no, path, message)
```

The script will then open a new tab in the web browser with the WhatsApp Web interface, and use PyAutoGUI to click on the appropriate buttons to send the document.

## Limitations
The script relies on PyAutoGUI to locate and click on specific elements of the WhatsApp Web interface, such as the "Attach" button and the "Send" button. This means that the script may not work properly if the interface changes, if the user has a different screen resolution, or if the script is run on a different computer. To mitigate these issues, the script uses the locateOnScreen() function with different confidence levels to locate the necessary images, and sets the confidence level lower if the image is not found after a certain number of attempts.

## Disclaimer
This script is for educational purposes only and should not be used for spamming or violating WhatsApp’s terms of service. I am not responsible for any consequences that may arise from using this script.

## License
This script is released under the MIT License. Feel free to use, modify, and distribute it as you see fit. However, please note that the script comes with no warranty or support, and the author is not responsible for any damage or liability caused by its use.
