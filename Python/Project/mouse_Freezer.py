import pyautogui
import time

# Get the initial position of the mouse cursor
original_x, original_y = pyautogui.position()

# Move the cursor to a new position
new_x, new_y = 500, 500
pyautogui.moveTo(new_x, new_y, duration=0.5)

# Simulate a hover effect
time.sleep(0.5)

# Move the cursor back to the original position
pyautogui.moveTo(original_x, original_y, duration=15)
