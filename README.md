# Daily-Quote-Email-Automation
Program written in Python which sends one random quote to think on every day.

# Prerequirements: 
Note: Only for linux/ mac. Haven't used in windows
- Gemini API:
    - Get the api_key from google gemini  
    ***Get Your Key From: [Link](https://aistudio.google.com/app/apikey)***
    - run Code:  
    ```bash
    export API_KEY="YOUR_API_KEY"
    ```
- Installations:
    Linux/Mac
    ```bash
    pip install smtplib
    pip install ssl
    pip install google.generativeai
    pip install email.mime.text
    ```
- Automation
    Linux/Mac
    ```bash
    crontab -e
    ```
    append the line  
    Note: this executes the code if the machine is active at 08:00 so change accordingly    
      
    P.S ***Change the /path/... to full path***
    ```bash
    0 8 * * * python /path/Daily-Quote-Email-Automation/project.py
    ```

# Development Documentation:
