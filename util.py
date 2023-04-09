import numpy as np
import cv2

# Function to define lower and upper limit of color palate
def get_limits(color):
    # Change dtype into unit8
    c = np.uint8([[color]])
    # Convert BGR to HSV
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    # Define lower and upper limit
    lowerLimit = hsvC[0][0][0] - 5, 100, 100
    upperLimit = hsvC[0][0][0] + 5, 255, 255

    # Convert to numpy array
    LowerLimit = np.array(lowerLimit, dtype=np.uint8)
    UpperLimit = np.array(upperLimit, dtype=np.uint8)

    # Return color palate lower and upper limit
    return LowerLimit, UpperLimit
