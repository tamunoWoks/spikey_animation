# Import modules
import time  # For adding delays between prints
import sys   # For exiting the program cleanly

try:
    while True:  # The main program loop runs indefinitely
        # Draw lines with increasing length (from 1^2 to 8^2 dashes)
        for i in range(1, 9):
            print('-' * (i * i))   # Print a line with i² dashes
            time.sleep(0.1)        # Wait 0.1 seconds to control animation speed
