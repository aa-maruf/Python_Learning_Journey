""" 
2. Go to Bored API (https://www.boredapi.com/) and read the documentation. Write a code that will suggest some activities every 30 minute and show as notification. 
Hint: In windows you can use win10toast or similar libraries to show notification on windows.
 """
from win10toast import ToastNotifier
import time
import requests


def get_activity():
    response = requests.get("http://www.boredapi.com/api/activity/")
    data = response.json()
    return data["activity"]

def notification():
    activity = get_activity()
    while(True):
        toaster = ToastNotifier()
        toaster.show_toast("Hello World!!!",
                        "Notification comming in 10 seconds!",
                        duration=10)

        toaster.show_toast("Hello, Learner",
                        activity,
                        duration=5,)
        time.sleep(5)
        # Wait for threaded notification to finish
        # while toaster.notification_active(): time.sleep(0.1)

if __name__ == '__main__':
    notification()