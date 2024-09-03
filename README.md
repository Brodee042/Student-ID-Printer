Student ID Printer Automation

This Python application automates the process of taking email requests and inputting the information into a student ID printer. The script searches for specific keywords in unread emails, extracts the relevant data, and automatically inputs the information into the student ID printer using a GUI interface.
Features

    Email Parsing: Automatically connects to an email account and checks for new, unread messages.
    Keyword Extraction: Extracts specific information such as address, delivery method, name, and student ID from the email content.
    Automatic Input: Automatically enters the extracted information into the student ID printer interface.
    User Interface: Simple Tkinter-based GUI for managing email checks and automatic printing.

Requirements

    Python 3.x
    Required Python libraries:
        imaplib
        email
        re
        pyautogui
        tkinter

You can install these dependencies using pip:

bash

pip install pyautogui

    Note: imaplib, email, re, and tkinter are part of the Python Standard Library, so you don't need to install them separately.

Setup

    Clone the Repository:

    bash

git clone https://github.com/yourusername/student-id-printer.git
cd student-id-printer

Configure Email Settings:

    Open the script and configure the following variables with your email server details:

    python

    EMAIL_HOST = 'your-email-host'
    EMAIL_USER = 'your-email@example.com'
    EMAIL_PASS = 'your-email-password'

    Security Note: To protect your email password, consider using environment variables or a separate configuration file that is not included in your version control.

Run the Application:

    Execute the script to start the application:

    bash

        python student_id_printer.py

Usage

    Check for Emails:
        Click the "Check for emails" button in the GUI. The script will check for any unread emails in your inbox and extract relevant information.

    Automatically Print ID:
        Click the "Automatically print out an ID, check page formatting" button. The application will input the extracted information into the student ID printer interface.
        The extracted data includes fields like "Address," "Delivery," "Name," and "Student ID." The script uses pyautogui to simulate mouse movements and keystrokes to input the information.

    Manual Verification:
        After the automation is complete, manually verify the information before printing to ensure accuracy.
