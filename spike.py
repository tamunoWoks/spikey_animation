# Import modules
import time  # For adding delays between prints
import sys   # For exiting the program cleanly

# Introduce constants
DELAY = 0.1         # Time delay between each frame (in seconds)
CHAR = '-'          # Character to use for drawing
MAX_INDEX = 8       # Maximum index (will square this value for line length)

try:
    while True:
        # Draw lines with increasing length (1^2 to MAX_INDEX^2)
        for i in range(1, MAX_INDEX + 1):
            print(CHAR * (i * i))  # Print line with i² characters
            time.sleep(DELAY)

        # Draw lines with decreasing length ((MAX_INDEX - 1)^2 to 2^2)
        for i in range(MAX_INDEX - 1, 1, -1):
            print(CHAR * (i * i))  # Print line with i² characters
            time.sleep(DELAY)

# Gracefully exit the program when the user presses Ctrl+C
except KeyboardInterrupt:
    sys.exit()
