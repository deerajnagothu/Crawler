import pyautogui
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
print(pyautogui.size())
width, height = pyautogui.size()
pyautogui.FAILSAFE = False
t = 75  # set a threshold value for origin points to click


def html_get_value(html_line):  # get value from a html line. Like "<span class="th" jscontent="pid" jstcache="12">3944</span>" will return 3944
    x=list(html_line)
    c=0
    if len(x)==0:
        return "Nothing"
    else:
        return x[0]


def get_tab_data(flag, already_open):
    if flag == 1:
        browser.find_element_by_tag_name("body").send_keys(Keys.CONTROL + "t")
        print(browser.window_handles)
        handle = browser.window_handles
        newly_opened_tab_handle = [ x for x in handle if x not in already_open]
        print(newly_opened_tab_handle)
        browser.switch_to_window(newly_opened_tab_handle[0])
        # browser.switch_to_window(new_tab)
        browser.get('chrome://memory')
        html = browser.page_source
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find_all("tr", jsselect="child_data")
        pid = []
        process_type = []
        page_name = []
        for each in table:
            print("PID:  "+(html_get_value(each.find(jstcache="12"))))
            pid.append(html_get_value(each.find(jstcache="12")))
            print("Process Type:  "+html_get_value(each.find(jstcache="18")))
            process_type.append(html_get_value(each.find(jstcache="18")))
            print("Page:  "+html_get_value(each.find(jstcache="22")))
            page_name.append(html_get_value(each.find(jstcache="22")))
            print("Total Memory:  "+html_get_value(each.find(jstcache="15")))
            print("Total Virtual Memory:  "+html_get_value(each.find(jstcache="17")))
            print("\n")
    sleep(3)
    browser.find_element_by_tag_name("body").send_keys(Keys.CONTROL + "w")
    sleep(2)
    browser.switch_to_window(already_open[0])
    browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
    sleep(1)
    print("The window handle after TAB is : "+str(browser.current_window_handle))
    check_tabs = browser.window_handles
    for tab_num in range(len(check_tabs)-1,0,-1):
        print("The tab going to be closed is : "+str(check_tabs[tab_num]))
        sleep(2)
        browser.switch_to_window(check_tabs[tab_num])
        print("The current window handle is : "+str(browser.current_window_handle))
        sleep(3)
        print("THis is the URL of this page : "+str(browser.current_url))
        sleep(3)
        browser.find_element_by_tag_name("body").send_keys(Keys.CONTROL + "w")
        sleep(2)
        print("Tab was closed an the remaining tabs are "+str(browser.window_handles))
        sleep(2)


    browser.switch_to_window(already_open[0])
    print("Switched to the main handle")
    sleep(3)
    return 0


def open_new_tab(flag):
    if flag == 1:
        browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    return True


def generate_coordinates(width, height, coordinates): # use the dimensions of the screen and generate coordinates(x,y) based on a threshold value
    difference=100
    for i in range(75, width, difference):
        for j in range(75, height, difference):
            coordinates.append(i)
            coordinates.append(j)
    temp=[]
    temp_coordinates=[]
    for i in range(0, len(coordinates)):
        if i%2==0:
            temp.append(coordinates[i])
            temp.append(coordinates[i+1])
            temp_coordinates.append(temp)
            temp=[]
    coordinates=temp_coordinates
    return coordinates


def generate_random_coordinates(coordinates): # shuffle the coordinates to generate random coordinates
    temp_coordinates=[]
    temp=[]
    for i in range(0, len(coordinates)):
        temp.append(i)
    for i in range(0, len(coordinates)):
        x=random.choice(temp)
        temp_coordinates.append(coordinates[x])
        temp.remove(x)
    coordinates=temp_coordinates
    return coordinates


def clicker(coordinate):  # generate click event on a particular coordinate
    x=coordinate
    pyautogui.keyDown('ctrlleft')
    print(x)
    pyautogui.moveTo(x[0],x[1],duration=0.1)
    pyautogui.click(x[0],x[1])
    pyautogui.keyUp('ctrlleft')
    return True


coordinates = []
coordinates = generate_coordinates(width,height,coordinates)

coordinates=generate_random_coordinates(coordinates)
browser=webdriver.Chrome("C:\\Users\Deeraj Nagothu\Desktop\Github\Crawler\chromedriver.exe") # change this according to the location of the "chromedriver.exe"
#browser.get('https://www.amazon.com')
browser.get('https://www.amazon.com')
browser.maximize_window()
main_window = browser.current_window_handle
print("this is my main window : "+str(main_window))

#browser.find_element_by_tag_name("body").send_keys(Keys.CONTROL + "t")
#second_window = browser.window_handles[1]
#browser.switch_to_window(second_window)
#browser.get('https://www.google.com')
for coordinate in coordinates:
    clicked=clicker(coordinate)
    sleep(2)
    number_of_tabs = len(browser.window_handles)
    if( number_of_tabs == 1):
        sleep(1)
        continue
    else:
        already_open = browser.window_handles
        get_tab_data(1,already_open)
        sleep(2)
