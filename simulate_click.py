import pyautogui
import random
from selenium import webdriver
print(pyautogui.size())
width, height = pyautogui.size()
pyautogui.FAILSAFE = False
t = 75  # set a threshold value for origin points to click

def generate_coordinates(width,height,coordinates):
    difference=100
    for i in range(75,width,difference):
        for j in range(75,height,difference):
            coordinates.append(i)
            coordinates.append(j)
    temp=[]
    temp_coordinates=[]
    for i in range(0,len(coordinates)):
        if(i%2==0):
            temp.append(coordinates[i])
            temp.append(coordinates[i+1])
            temp_coordinates.append(temp)
            temp=[]
    coordinates=temp_coordinates
    return coordinates

def generate_random_coordinates(coordinates):
    temp_coordinates=[]
    temp=[]
    for i in range(0,len(coordinates)):
        temp.append(i)
    for i in range(0,len(coordinates)):
        x=random.choice(temp)
        temp_coordinates.append(coordinates[x])
        temp.remove(x)
    coordinates=temp_coordinates
    return coordinates
def clicker(flag,coordinates):
    if (flag == 1):
        for x in coordinates:
            pyautogui.keyDown('ctrlleft')
            print(x)
            pyautogui.moveTo(x[0],x[1],duration=0.1)
            pyautogui.click(x[0],x[1])
            pyautogui.keyUp('ctrlleft')

coordinates=[]
coordinates=generate_coordinates(width,height,coordinates)
print (len(coordinates))
print (coordinates)
coordinates=generate_random_coordinates(coordinates)
print("########################")
print(len(coordinates))
print(coordinates)
browser=webdriver.Firefox()
browser.get('https://www.flipkart.com')
browser.maximize_window()
clicker(1,coordinates)
