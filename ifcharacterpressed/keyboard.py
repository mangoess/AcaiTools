# This program will print "Hi!" once you press the "H" key, with a cooldown of 5 seconds.
import keyboard # You'll need to install this with pip first, you can see a tutorial if you're interested!
import time # Module installed with Python automatically, no need to install it with pip.

cooldown = '0' # Set's the cooldown to 0 before the program starts.
while True:
    if keyboard.is_pressed("h"):
        if cooldown == '0': # Checking if there is no cooldown
            print("Hi!")
            cooldown = '1'
            time.sleep(5) # The cooldown of how long till the cooldown is reset
            cooldown = '0'
        elif cooldown == '1': # If there is a cooldown, it will be regarded as 1, then it passes. 
            pass # Essentially a command that just skips and waits till you press h again!
