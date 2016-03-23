import pyautogui
print (pyautogui.size())
width,height=pyautogui.size()
pyautogui.FAILSAFE = False
for i in range(5):
      pyautogui.moveTo(100, 100, duration=1)
      pyautogui.doubleClick(100,100)
      pyautogui.moveTo(2560, 100, duration=1)
      pyautogui.moveTo(2560, 1440, duration=1)
      pyautogui.moveTo(100, 2560, duration=1)
