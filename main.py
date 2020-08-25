import pyautogui
from PIL import ImageGrab
import time

while True:
    px = ImageGrab.grab().load()
    if px[1899, 1000] == (0, 100, 163):
        time.sleep(1)
        pyautogui.click(145, 1025)
    time.sleep(2)
