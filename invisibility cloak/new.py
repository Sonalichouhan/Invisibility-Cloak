#this file is used to identify the hsv values of any image
import cv2
import numpy as np

# Load the image
image = cv2.imread(r"C:\Users\ASUS\OneDrive\Pictures\Screenshots\hsv.png")


# Convert the image to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Function to display HSV values on mouse click
def get_hsv(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse button click
        hsv_value = hsv_image[y, x]  # Get HSV value at clicked point
        print(f"HSV Value at ({x}, {y}): {hsv_value}")

# Display the image
cv2.imshow("Image", image)
cv2.setMouseCallback("Image", get_hsv)

# Wait until a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
