
""" 
4. Create a chat bot that will understand if you are bored, then it will call the Bored API and suggest some activities to you in reply.
 It should also have the ability to tell the current time.

Example:
>> Hey robot, this house is boring. Any idea what I can do?
Bot:  You can learn Javascript.
>> thank you. What’s the time?
Bot: it’s 9:30 pm sir. 
"""

import datetime
import requests
import time

bored_msg = ["bore", "boring", "bored"]
time_msg = ["time", "clock"]

def get_activity():
    response = requests.get("http://www.boredapi.com/api/activity/")
    data = response.json()
    return data["activity"]
while True:
    user_msg = input(">> ")
    for word in bored_msg:
        if word in user_msg.lower():
            activity = get_activity()
            print("Bot :" + activity)
    for word in time_msg:
            if word in user_msg.lower():
                now = datetime.datetime.now().strftime('%I:%M %p')
                print("Bot : " + now)
    time.sleep(1)



