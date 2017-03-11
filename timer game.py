import time
from timeit import default_timer
print "WELCOME"
print " \t Time game"
print """
Instructions:
    1.Timer will start when you say start and press enter.
    2.Count to certain seconds (your choice) in your head.
    3.Press enter to stop the timer.
    4.Check the timer to see how close you were.
"""
def start():
    print "Starting..."
    time.sleep(1.5)
    print "Choose the amount of seconds"
    time.sleep(1)
    print"Type start and press enter"
    start=raw_input("")
    if start=="start":
        starttimer=default_timer()
        print "Press enter when you think specific seconds have passed by"
        stop=raw_input("")
        if stop=="":
            timerstop=default_timer()-starttimer
            print "Seconds passed by:",timerstop
            time.sleep(0.5)
            print "Hope you were close"
            time.sleep(1)
        print "Thanks for your Playing"
    else:
        print "Type start and press enter"
start()
        
