import pyautogui
import time
from datetime import datetime

print("5 Second Timer till location outputted")
time.sleep(1)
print("5 Seconds completed, Starting program")
while True:
    time.sleep(2)
    location = CurrentMouseX, currentMouseY = pyautogui.position()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Location is", location, "Time of capturing is", current_time)
