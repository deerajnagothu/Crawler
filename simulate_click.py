import pyautogui
from selenium import webdriver
print(pyautogui.size())
width, height = pyautogui.size()
pyautogui.FAILSAFE = False
t = 75  # set a threshold value for origin points to click


def clicker(flag):
    if (flag == 1):
        pyautogui.keyDown('ctrlleft')
        for i in range(0, width, 50):
            for j in range(0, height, 50):
                print(t+j,t+i)
                pyautogui.moveTo(t + j, t + i, duration=0.1)
                pyautogui.click(t + j, t + i)
        pyautogui.keyUp('ctrlleft')


"""
for i in range(5):
      pyautogui.moveTo(100, 100, duration=1)
      pyautogui.doubleClick(100,100)
      pyautogui.moveTo(2560, 100, duration=1)
      pyautogui.moveTo(2560, 1440, duration=1)
      pyautogui.moveTo(100, 2560, duration=1)
"""
browser=webdriver.Firefox()
browser.get('https://www.flipkart.com')
clicker(1)
