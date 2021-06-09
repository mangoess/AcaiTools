import pyautogui # To find the location of the position of your mouse
import time # Just to time
from datetime import datetime # The module to get the date / time that is in the message

print("3 Second Timer till location outputted")
time.sleep(3)
print("3 Seconds completed, Starting program")
while True:
    time.sleep(2) # Updates and gives a new position every 2 seconds.
    location = CurrentMouseX, currentMouseY = pyautogui.position()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current location of mouse cursor is", location, "the time this was captured on is current_time")
   
# Please make a pull request if you'd like to change a part of the code, I'd love your opinions.
# MADE BY MANGOESS
# INSPIRED BY SUPELION
