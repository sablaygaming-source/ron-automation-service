import requests
import json
import threading
import sys

# Replace this with your ACTIVE Webhook URL from Make.com
MAKE_WEBHOOK_URL = "https://hook.eu1.make.com/1s442riabjmpt3dubtwyv9hadn815ek1"
exit_event = threading.Event()

startProcess = False

# The data you want to send
payload = {
    "sender_name": "Ron",
    "recipient": "migelbonie@gmail.com",
    "message": "blank",
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

def fInputInfo(pPrompt):#2

    while True: #3
        ch = input(f"\npress b to back, enter {pPrompt}: ")
        if ch == '':#4
            print(f"\nblank input is not valid")
            continue
        #5
        return ch
    #3
#2
def fMain(): #2
    
    global exit_event
    global startProcess
    print("Initiating email blast via Make.com...")
    
    # Inside fMain, when you start the thread:
    background_thread = threading.Thread(target=fAutomationTask, args=(exit_event,))
    background_thread.start()
    

    # 3. Main Thread (Thread B) stays here in standby mode
    print("System is running..")

    vIndex = 0
    while True: #3
        print(f"\ninformation last email: {payload['recipient']}\nlast message {payload['message']}")
        ch= input(f"\ninput q to leave, main menu i input new send set ")
        
        if ch.lower() == 'q':#4            

            #set daemon = True to force it to close, and not finishing the function work
            # threading.Thread(target=fAutomationTask, daemon= True) 
            exit_event.set()
            background_thread.join()
            print("\nexiting prog...")
            sys.exit()    
            return
        
        elif ch.lower() == 'i': #4
            #input process    
            startProcess = False
            vEmail = fInputInfo("Email")
                
            if vEmail.lower() == 'b':#10
                
                continue        
            #10
            
            payload['recipient'] = vEmail
            
            vMessage = fInputInfo("Message")
                
            if vMessage.lower() == 'b':#10
                continue        
            #10
            
            payload['message'] = vMessage

            startProcess = True
        #4
    #3
#2

fMain()


