# This program will print "Hi!" once you press the "H" key

import keyboard # You'll need to install this with pip first, you can see a tutorial if you're interested!

while True:
    if keyboard.is_pressed("h"):
        print("Hi!")
        pass # Essentially a command that just skips and waits till you press h again!