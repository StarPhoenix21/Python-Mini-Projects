import time
from datetime import datetime

def reminder(message, remindAt):
    """Set a reminder for a specific time."""
    print(f"Your Task Reminder is Activated !!!\n[Time : {remindAt} | Task : {message}]\n\nNow : {datetime.now().strftime('%H:%M')}")
    while True:
        if str(datetime.now().strftime('%H:%M')) == remindAt:
            print(f"Reminder: {message}")
            break
        time.sleep(10)

"""
time format should be like ["00:00"] - > ["06:51"]
"""
reminder("Attend meeting", "06:51")
