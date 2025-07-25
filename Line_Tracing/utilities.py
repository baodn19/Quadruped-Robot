import cv2
import numpy as np

def thresholding(image):
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define thresholds for white color in HSV
    lower_white = np.array([0, 0, 0])
    upper_white = np.array([179, 255, 255])
    mask_white = cv2.inRange(image_hsv, lower_white, upper_white)

    return mask_white