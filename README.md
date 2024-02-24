# IBAN Detector

This repository contains a Python script for detecting International Bank Account Numbers (IBANs) from the clipboard content.

## Description

The script continuously monitors the clipboard for any new content. If the content matches the structure of an IBAN, it replaces the clipboard content with a predefined IBAN from the environment variables.

## Usage

1. Clone this repository.
2. Install the required Python packages: `pyperclip` and `python-dotenv`.
3. Set your preferred IBAN in the environment variable "IBAN".
4. Run the script.

## Code

The main function `iban_detecter` uses a regular expression to match the structure of an IBAN. If an IBAN is detected in the clipboard content, it is replaced with the IBAN from the environment variable.

## Disclaimer

This program is for educational purposes only. Please do not use it for any illegal activities. The author is not responsible for any misuse of this program.
