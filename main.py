import requests
import json
import sys
import os
import time

#libraries for date
from datetime import date, time, datetime

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

def fAutomationTask(stop_event): #2
    """This function runs in the background (Thread A)"""
    global startProcess
    print("\n--- Background Automation Started ---")
    
    while not stop_event.is_set():#10
        # wait() returns True if the event was set (q was pressed)
        # and False if the timer just ran out normally

        #print(f"\ndebug before while dSec")

        dSec = 0
        while dSec < 60 : #11

            stop_event.wait(timeout=1)

            #print(f"\ndebug {dSec= }")    
            
            #standby
            if startProcess == False:#12
                while not startProcess :#14
                    pass #to stand by here
                #14
                print(f"\nstarting to count in 60 seconds")
                dSec = 0 
            #12
            dSec += 1
        #11

        fSendData()
            
    #10
    
    print("\nBackground thread safely stopped.")
    
    
#2

def fMain(): #2
    
    print("start running main")

    vIndex = 0
    while True: #3

        while dSec < 60: #4
            time.sleep(1)
        #4
        compDateTime = datetime.now()
        payload["message"] = f"{compDateTime.strftime("Date: %Y-%m-%d \nTime: %H:%M:%S=")}\nTo whom it may concern\nsended email for testing...\n\nthanks\nron sm" 
        fSendData()
    #3

#2

fMain()


