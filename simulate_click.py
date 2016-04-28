import pyautogui
import random
from selenium import webdriver
from bs4 import BeautifulSoup
print(pyautogui.size())
width, height = pyautogui.size()
pyautogui.FAILSAFE = False
t = 75  # set a threshold value for origin points to click

def html_get_value(str):  #get value from a html line. Like "<span class="th" jscontent="pid" jstcache="12">3944</span>" will return 3944
    x=list(str)
    c=0
    if(len(x)==0):
        return "Nothing"
    else:
        return(x[0])

def get_tab_count
def generate_coordinates(width,height,coordinates): #use the dimensions of the screen and generate coordinates(x,y) based on a threshold value 
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

def generate_random_coordinates(coordinates): #shuffle the coordinates to generate random coordinates 
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
def clicker(flag,coordinate):  #generate click event on a particular coordinate
    if (flag == 1):
        x=coordinate
		pyautogui.keyDown('ctrlleft')
        print(x)
        pyautogui.moveTo(x[0],x[1],duration=0.1)
        pyautogui.click(x[0],x[1])
        pyautogui.keyUp('ctrlleft')


coordinates=[]
coordinates=generate_coordinates(width,height,coordinates)

coordinates=generate_random_coordinates(coordinates)
#browser=webdriver.Firefox()
browser=webdriver.Chrome("C:\\Users\Deeraj Nagothu\Desktop\Github\Crawler\chromedriver.exe")
browser.get('https://www.amazon.com')
browser.maximize_window()
for coordinate in coordinates:
    clicked=clicker(1,coordinate)
	