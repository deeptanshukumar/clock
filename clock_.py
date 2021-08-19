from turtle import *
import time
seconds = 0
minutes = 28
hours = 7


setup()
t1 = Turtle()
while True:
    t1.clear()
    t1.write(str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" +
             str(seconds).zfill(2), font=("segoe ui light", 45, "normal"))
    seconds = seconds + 1
    time.sleep(1)
    if seconds == 60:
        seconds = 0
        minutes = minutes + 1
    if minutes == 60:
        minutes = 0
        hours = hours + 1
