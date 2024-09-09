import smtplib
import ssl
import re
from os import getenv
import google.generativeai as genai
from email.mime.text import MIMEText

def main():
    # GEMINI GENERATION
    genai.configure(api_key=getenv('API_KEY'))
    model = genai.GenerativeModel('gemini-1.5-flash')
    subject = "Thought For The Day"
    response = model.generate_content(f"Prompt: Give me only single line output. \"{subject}\"",)
    
    message = f"Subject: {subject}\n\n{response.text}"
    sender, passkey, receivers = inputFromFile("info.txt")
    msg = MIMEText(message)
    msg['From'] = "Your Friendly Reminder"
    error = send_mail(sender, passkey, *receivers, message = message)

    if error:
        print("Failed to send email to the following addresses:")
        for address in error:
            print(address)
    else:
        print("Sent all mail successfully")

def inputFromFile(fileLink):
    file = open(fileLink, "r")
    sender_mail = ""
    sender_passkey = ""
    match = []

    for line in file:
        if "sender" in line:
            if sender_mail == "":
                sender_mail = re.search(r'"([^"]*)"', line).group(1)
            else:
                raise Exception("More than one sender email provided.\n Read \"readme.py\" for proper use instructions.")
        elif "passkey" in line:
            if sender_passkey == "":
                sender_passkey = re.search(r'"([^"]*)"', line).group(1)
            else:
                raise Exception("More than one passkey provided.\n Read \"readme.md\" file for proper use instructions.")
        elif "receiver" in line:
            match.append(re.search(r'"([^"]*)"', line).group(1))
    file.close()
    return sender_mail, sender_passkey, match

def send_mail(sender_email, sender_passkey, *receiver_emails, message) -> list:
    context = ssl.create_default_context()
    
    error = []
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        try:
            server.login(sender_email, sender_passkey)
        except Exception as e:
            print(f"{e}\nIncorrect passkey or email. Set up correctly as instructed in the 'readme.md' file.")
            return receiver_emails 

        for receiver_mail in receiver_emails:
            try:
                server.sendmail(sender_email, receiver_mail, message)
                print(f"Email sent successfully to {receiver_mail}!")
            except Exception as e:
                print(f"{e}\nFailed to send email to {receiver_mail}:")
                error.append(receiver_mail)
                
    return error

if __name__ == "__main__":
    main()

