import imaplib
import email
import re
import pyautogui
import time
import tkinter as tk

def search_email(extracted_words, empty_label):
    EMAIL_HOST = ''
    EMAIL_USER = ''
    EMAIL_PASS = ''

    # Connect to the Email Server
    my_mail = imaplib.IMAP4_SSL(EMAIL_HOST)
    my_mail.login(EMAIL_USER, EMAIL_PASS)

    # Select the  mailbox aka INBOX
    my_mail.select('INBOX')

    # Search for Unseen emails, put SEEN if you want to check all former emails aswell
    _, data = my_mail.search(None, 'UNSEEN')

    # empty list to capture all messages
    # extract data into the msgs list
    msgs = []

    # IDs of all emails that we want to fetch, then we read the first unread email with data added to msgs
    unread_mail_id_list = data[0].split()
    if unread_mail_id_list:
        first_unread_email_id = unread_mail_id_list[0]

    for first_unread_email_id in unread_mail_id_list:
        typ, data = my_mail.fetch(first_unread_email_id, '(RFC822)')  # RFC822 returns whole message
        msgs.append(data)

    # Get text from emails and extract words after keywords
    get_text_from_email(msgs, extracted_words)

    if not extracted_words:
        empty_label.config(text="The list is empty")
    else:
        empty_label.config(text="Their are unprinted messages, continue")


def extract_words_after_keywords(text, keywords):
    words_after_keywords = []
    for keyword in keywords:
        pattern = r'.*?\b' + re.escape(keyword) + r'\b(.*)'
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        words_after_keywords.extend(matches)
    return words_after_keywords

def get_text_from_email(msgs, extracted_words):
    keywords_to_find = ['Address: ', 'Delivery: ', 'Name: ', 'Student ID: ']
    for msg in msgs[::-1]:
        for response_part in msg:
            if isinstance(response_part, tuple):
                my_msg = email.message_from_bytes(response_part[1])

                # Get the plain text body of the email
                body = ''
                for part in my_msg.walk():
                    if part.get_content_type() == 'text/plain':
                        body = part.get_payload()

                # Extract words after keywords and add to the extracted_words list
                extracted_words.extend(extract_words_after_keywords(body, keywords_to_find))

def auto_clicker(extracted_words, empty_label):
    if not extracted_words:
        empty_label.config(text="The list is empty")
        return

    else:
        IndexPosition = 0

        #Address
        time.sleep(5)
        pyautogui.moveTo(1000, 1000, duration=1)
        pyautogui.click()
        pyautogui.typewrite(extracted_words[IndexPosition])
        extracted_words.pop(IndexPosition)

        #Delivery
        pyautogui.moveTo(1100, 1100, duration=1)
        pyautogui.click()
        pyautogui.typewrite(extracted_words[IndexPosition])
        extracted_words.pop(IndexPosition)

        #Name
        pyautogui.moveTo(1200, 1200, duration=1)
        pyautogui.click()
        pyautogui.typewrite(extracted_words[IndexPosition])
        extracted_words.pop(IndexPosition)

        #Student ID
        pyautogui.moveTo(1300, 1300, duration=1)
        pyautogui.click()
        pyautogui.typewrite(extracted_words[IndexPosition])
        extracted_words.pop(IndexPosition)
        empty_label.config(text="manually double check all information")

        if not extracted_words:
            empty_label.config(text="The list is empty")


def main():
    # Create the main application window
    root = tk.Tk()
    root.title("Button Functions")

    # Get initial values for extracted_words
    extracted_words = []

    # Create the buttons and assign functions to them
    button1 = tk.Button(root, text="Check for emails", command=lambda: search_email
    (extracted_words, empty_label))

    button2 = tk.Button(root, text="Automatically print out an ID, check page formatting",
                        command=lambda: auto_clicker(extracted_words, empty_label))

    # Place the buttons on the window using a grid layout
    button1.grid(row=0, column=0, padx=10, pady=5)
    button2.grid(row=0, column=1, padx=10, pady=5)

    empty_label = tk.Label(root, text="", fg="red")
    empty_label.grid(row=1, column=0, columnspan=2, padx=10, pady=5)


    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    main()

# def auto_clicker(extracted_words):
#     zero = 0
#     values = True
#     while values == True:
#         if not extracted_words:
#             print("The list is empty")
#             values = False
#             break
#         else:
#             IndexPosition = 0
#
#             time.sleep(5)
#             pyautogui.moveTo(1000, 1000, duration=1)
#             pyautogui.click()
#             pyautogui.typewrite(extracted_words[IndexPosition])
#             extracted_words.pop(zero)
#
#             pyautogui.moveTo(1100, 1100, duration=1)
#             pyautogui.click()
#             pyautogui.typewrite(extracted_words[IndexPosition])
#             extracted_words.pop(zero)
#
#             pyautogui.moveTo(1200, 1200, duration=1)
#             pyautogui.click()
#             pyautogui.typewrite(extracted_words[IndexPosition])
#             extracted_words.pop(zero)
#
#             pyautogui.moveTo(1300, 1300, duration=1)
#             pyautogui.click()
#             pyautogui.typewrite(extracted_words[IndexPosition])
#             extracted_words.pop(zero)
#
#             if not extracted_words:
#                 print("The list is empty")
#                 values = False

#
#
# # Print the extracted words after the keywords, comment out this section in final version
# print("Extracted Words After Keywords:")
# print(extracted_words)


# The code below prints the contents of the entire email

# for msg in msgs[::-1]:
#    for response_part in msg:
#        if type(response_part) is tuple:
#            my_msg=email.message_from_bytes((response_part[1]))
#            print("_________________________________________")
#            #print ("subj:", my_msg['subject'])
#            #print ("from:", my_msg['from'])
#            print ("body:")
#            for part in my_msg.walk():
#                #print(part.get_content_type())
#                if part.get_content_type() == 'text/plain':
#                    print (part.get_payload())

