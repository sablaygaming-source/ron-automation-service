import requests
import json
import sys
import os
import time

#libraries for date
from datetime import datetime

# Replace this with your ACTIVE Webhook URL from Make.com

MAKE_WEBHOOK_URL = os.environ.get('MAKE_WEBHOOK_URL')

#MAKE_WEBHOOK_URL = "https://hook.eu1.make.com/1s442riabjmpt3dubtwyv9hadn815ek1"


# The data you want to send
payload = {
    "sender_name": "Ron",
    "recipient": "migelbonie@gmail.com",
    "message": "",
    "status": "Success"
}

headers = {
    "Content-Type": "application/json"
}

def fSendData():#2
    print("\n\nnow sending...")
    try:
        response = requests.post(
            MAKE_WEBHOOK_URL, 
            data=json.dumps(payload), 
            headers=headers
        )

        if response.status_code == 200:
            print(f"✅ Success! Make.com is now sending the email to {payload['recipient']}")
        else:
            print(f"❌ Failed. Error code: {response.status_code}")
            # If you see 410, remember to click 'Re-determine data structure' in Make
            print("Response Text:", response.text)

    except Exception as e:
        print(f"Connection Error: {e}")

#2

def fMain(): #2
    
    print("start running main")

    vTotalSec = 30
    while True: #3
        dSec = 0
        print()
        while dSec < vTotalSec: #4
            time.sleep(1)
            print(f"loop running at {dSec}")
            dSec +=1
        #4
        compDateTime = datetime.now()
        print(f"\ni will send it at datetime\n{compDateTime.strftime("Date: %Y-%m-%d \nTime: %H:%M:%S")}")
        payload["message"] = f"{compDateTime.strftime("Date: %Y-%m-%d \nTime: %H:%M:%S")}<br><br>To whom it may concern<br>     sended email for testing...<br><br><br>thanks<br>ron sm" 
        fSendData()
    #3

#2

fMain()


