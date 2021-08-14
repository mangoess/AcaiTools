import pyautogui # To find the location of the position of your mouse
import time # Just to time
from datetime import datetime # The module to get the date / time that is in the message

button = '[' # CHANGE THE "[" INSIDE THE APOSTROPHES ' TO CHANGE THE BUTTON.
print("Program Ready, Click", button, "to output the coordinates!")
while True: 
    try:
        if keyboard.is_pressed(button):  # if the selected button is pressed
            location = CurrentMouseX, currentMouseY = pyautogui.position()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("\n\nCurrent location of mouse cursor is", location, "the time this was captured on is", current_time)
            time.sleep(5)
    except:
        pass

# Please make a pull request if you'd like to change a part of the code, I'd love your opinions.
# MADE BY MANGOESS, V 0.2
# INSPIRED BY SUPELION
