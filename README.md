# Daily-Quote-Email-Automation
Program written in Python which sends one random quote to think on every day.

# Prerequirements: 
Note: **Only for linux/ mac.** Haven't used in windows
- Open the info.txt file and replace passkey with appkey from [Passkey](https://www.zdnet.com/article/gmail-app-passwords-what-they-are-how-to-create-one-and-why-to-use-them/) for sender mail.
- make the *"info.txt"* format like (Replace values): 
    ```txt
    sender = "sendermai@gmail.com"
    passkey = "sendermail_passkey"
    receiver = "example0@gmail.com"
    receiver = "example1@proton.me"
    receiver = "example2@gmail.com"
    ```
- Gemini API:
    - Get the api_key from google gemini  
    ***Get Your Key From: [Link](https://aistudio.google.com/app/apikey)***
    - run Code:  
    ```bash
    export API_KEY="YOUR_API_KEY" # replace the YOUR_API_KEY with actual key, keeping it in the "..."
    ```
- Installations:
    ```bash
    pip install google.generativeai
    ```
- Automation
    ```bash
    crontab -e
    ```
    append the line  
    Note: this executes the code if the machine is active at 08:00 so change accordingly    
      
    P.S ***Change the /path/... to full path***
    ```bash
    0 8 * * * python /path/Daily-Quote-Email-Automation/project.py
    ```