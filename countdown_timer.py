# Ward - Countdown Timer
# Created 08/03/2024

import time

def countdown(time_sec):
    # Continue the loop as long as there's time remaining
    while time_sec:
        # Divide the total seconds into minutes and remaining seconds
        mins, secs = divmod(time_sec, 60)
        
        # Format the time as MM:SS
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        
        # Print the formatted time, overwriting the previous line
        print(timeformat, end='\r')
        
        # Pause for 1 second
        time.sleep(1)
        
        # Decrease the remaining time by 1 second
        time_sec -= 1
    
    # When the countdown finishes, print "stop"
    print("stop")

# Start the countdown with 60 seconds
countdown(60)