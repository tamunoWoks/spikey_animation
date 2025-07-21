# Import modules
import time  # For adding delays between prints
import sys   # For exiting the program cleanly

# Introduce constants
DELAY = 0.1         # Time delay between each frame (in seconds)
CHAR = '-'          # Character to use for drawing
MAX_INDEX = 8       # Maximum index (will square this value for line length)

try:
    while True:  # The main program loop runs indefinitely
        # Draw lines with increasing length (from 1^2 to 8^2 dashes)
        for i in range(1, 9):
            print('-' * (i * i))   # Print a line with i² dashes
            time.sleep(0.1)        # Wait 0.1 seconds to control animation speed

        # Draw lines with decreasing length (from 7^2 to 2^2 dashes)
        for i in range(7, 1, -1):
            print('-' * (i * i))   # Print a line with i² dashes
            time.sleep(0.1)        # Wait 0.1 seconds again

# Gracefully exit the program when the user presses Ctrl+C
except KeyboardInterrupt:
    sys.exit()
