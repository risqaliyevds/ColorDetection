import numpy as np
import cv2
from util import *
from PIL import Image

# Video capture
cap = cv2.VideoCapture(0)
# yellow in BGR color spice
yellow = [0,255,255]

while True:
    rat, frame = cap.read()
    # Convert color from GBR to HSV
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Set upper end lower area of yellow
    LowerLimit, UpperLimit = get_limits(yellow)
    # Masking by upper and lower area. Camera detects only this color palate.
    mask = cv2.inRange(hsvImage, LowerLimit, UpperLimit)
    # Convert mask array to Image
    mask_ = Image.fromarray(mask)
    # Define image square points coordinate
    bbox = mask_.getbbox()
    # Draw bbox if yellow object exists
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        # Draw rectangle around object color green and size 5
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 5)

    # Final output
    cv2.imshow('frame', frame)

    # Setting to stop loop press 'q' keyboard
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
