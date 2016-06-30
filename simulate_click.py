# Author: Deeraj Nagothu, MS in ECE @Binghamton University
import pyautogui
import random
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep
from py2neo import Graph, Node, Relationship

print(pyautogui.size())
width, height = pyautogui.size()
pyautogui.FAILSAFE = False
t = 75  # set a threshold value for origin points to click
target = 'https://www.amazon.com'

def html_get_value(html_line):  # get value from a html line. Like "<span class="th" jscontent="pid" jstcache="12">3944</span>" will return 3944
    x = list(html_line)
    if len(x)==0:
        return "Nothing"
    else:
        return x[0]

def get_tab_data(flag, already_open):  #  open the new tab for memory data and get data
    if flag == 1:
        print("Entered the get tab data function")
        browser.find_element_by_tag_name("body").send_keys(Keys.CONTROL + "t")
       # print(browser.window_handles)
        handle = browser.window_handles
        newly_opened_tab_handle = [x for x in handle if x not in already_open]
       # print(newly_opened_tab_handle)
        browser.switch_to_window(newly_opened_tab_handle[0])
        # browser.switch_to_window(new_tab)
        browser.get('chrome-extension://eobmgbdhncfblmillcdjjnnbhcpjognj/popup.html')
        sleep(3)
        pyautogui.keyDown('shift')
        pyautogui.press('esc')
        pyautogui.keyUp('shift')
        x = pyautogui.size()
        y = int(x[0]/2)
        z = int(x[1]/2)
        pyautogui.click(y, z, button='right' )
        pyautogui.press('up')
        pyautogui.press('up')
        pyautogui.press('enter')
        sleep(2)
        html = browser.page_source
        soup = BeautifulSoup(html, "html.parser")

        pyautogui.press('esc')
        table = soup.find_all("tr")
        details = []

        for each in range(1, len(table)):
            # print(table[each].find_all("td"))
            x = table[each].find_all("td")
            print("Chrome PID is " + x[0].get_text())
            details.append(x[0].get_text())
            print("PID is "+x[1].get_text())
            details.append(x[1].get_text())
            print("Type is "+x[2].get_text())
            details.append(x[2].get_text())
            print("CPU Utilisation is "+x[3].get_text())
            details.append(x[3].get_text())
            print("Network Consumption is "+x[4].get_text())
            details.append(x[4].get_text())
            print("Title is "+x[5].get_text())
            text = str(x[5].get_text())
            print(text)
            # q = text.index("title")
            q = [i for i in range(len(text)) if text.startswith("title", i)]
            print("the position is"+str(q))
            if len(q) > 1:
                title = text[q[1]+8:len(text)-3]
                duplicate = True
            else:
                title = text[q[0]+8:len(text)-3]
                duplicate = False
            print("The final title is "+str(title))
            details.append(title)
            print("Private Memory is "+x[6].get_text())
            details.append(x[6].get_text())
            print("JavaScript Memory is "+x[7].get_text())
            details.append(x[7].get_text())

    sleep(3)
    browser.find_element_by_tag_name("body").send_keys(Keys.CONTROL + "w") # close the memory tab along with the newly opened tab.
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
        sleep(1)
        url = browser.current_url
        print("THis is the URL of this page : "+str(url))
        sleep(1)
        browser.find_element_by_tag_name("body").send_keys(Keys.CONTROL + "w")
        sleep(2)
        print("Tab was closed an the remaining tabs are "+str(browser.window_handles))
        sleep(2)


    browser.switch_to_window(already_open[0])
    print("Switched to the main handle")
    sleep(3)
    return details, url, duplicate

def get_initital_browser_data(flag,freshly_opened):
    if flag == 1:
        browser.find_element_by_tag_name("body").send_keys(Keys.CONTROL + "t")
       # print(browser.window_handles)
        handle = browser.window_handles
        print(handle)
        newly_opened_tab_handle = [x for x in handle if x not in freshly_opened]
       # print(newly_opened_tab_handle)
        browser.switch_to_window(newly_opened_tab_handle[0])
        # browser.switch_to_window(new_tab)
        browser.get('chrome-extension://eobmgbdhncfblmillcdjjnnbhcpjognj/popup.html')
        sleep(3)
        pyautogui.keyDown('shift')
        pyautogui.press('esc')
        pyautogui.keyUp('shift')
        x = pyautogui.size()
        y = int(x[0]/2)
        z = int(x[1]/2)
        pyautogui.click(y, z, button='right' )
        pyautogui.press('up')
        pyautogui.press('up')
        pyautogui.press('enter')
        sleep(3)
        html = browser.page_source
        soup = BeautifulSoup(html, "html.parser")

        pyautogui.press('esc')
        table = soup.find_all("tr")
        details = []

        for each in range(1, len(table)):
            # print(table[each].find_all("td"))
            x = table[each].find_all("td")
            print("Chrome PID is " + x[0].get_text())
            details.append(x[0].get_text())
            print("PID is "+x[1].get_text())
            details.append(x[1].get_text())
            print("Type is "+x[2].get_text())
            details.append(x[2].get_text())
            print("CPU Utilisation is "+x[3].get_text())
            details.append(x[3].get_text())
            print("Network Consumption is "+x[4].get_text())
            details.append(x[4].get_text())
            print("Title is "+x[5].get_text())
            text = str(x[5].get_text())
            q = text.index("title")
            title = text[q+8:len(text)-3]
            details.append(title)
            print("Private Memory is "+x[6].get_text())
            details.append(x[6].get_text())
            print("JavaScript Memory is "+x[7].get_text())
            details.append(x[7].get_text())
            print(x[7].get_text())

    sleep(3)
    browser.find_element_by_tag_name("body").send_keys(Keys.CONTROL + "w")
    sleep(2)
    browser.switch_to_window(freshly_opened[0])
    return details

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
    x = coordinate
    pyautogui.keyDown('ctrlleft')
    print(x)
    pyautogui.moveTo(x[0], x[1], duration=0.1)
    pyautogui.click(x[0], x[1])
    pyautogui.keyUp('ctrlleft')
    return True


def initial_draw_graph(details, gp):
    m = [details[x:x+8] for x in range(0, len(details), 8)] # split the details list into sublist of 8
    extensions = []
    plugins = []
    survivors = []
    # The following part is to create the Nodes
    for x in m:
        if x[2] == "browser":
            print("the browser list is:")
            print(x)
            browser = Node("Browser", name=x[5], PID=x[1], CPU=x[3], Network=x[4], Private_memory=x[6], JSmemory=x[7])
            gp.create(browser)
            survivors.append(x[1])
        elif x[2] == "gpu":
            print("the gpu list is")
            print(x)
            gpu = Node("GPU", name=x[5], PID=x[1], CPU=x[3], Network=x[4], Private_memory=x[6], JSmemory=x[7])
            gp.create(gpu)
            survivors.append(x[1])
        elif x[2] == "extension":
            print("the extension list is")
            print(x)
            node = Node("Extension", name=x[5], PID=x[1], CPU=x[3], Network=x[4], Private_memory=x[6], JSmemory=x[7])
            gp.create(node)
            extensions.append(node)
            if x[5] != "Extension: chrome-extension://eobmgbdhncfblmillcdjjnnbhcpjognj/popup.html":
                survivors.append(x[1])
        elif x[2] == "renderer":
            print("the renderer list is")
            print(x)
            main_tab = Node("Main Tab", name=x[5], PID=x[1], CPU=x[3], Network=x[4], Private_memory=x[6], JSmemory=x[7])
            gp.create(main_tab)
            survivors.append(x[1])
        elif x[2] == "plugin":
            print("the plugin list is")
            print(x)
            node = Node("Plugin", name=x[5], PID=x[1], CPU=x[3], Network=x[4], Private_memory=x[6], JSmemory=x[7])
            gp.create(node)
            plugins.append(node)
            survivors.append(x[1])
    # The following part is to create the relationship between the browser initial stage
    rel1 = Relationship(main_tab,"GPU",gpu)
    gp.create(rel1)
    rel2 = Relationship(main_tab,"Browser",browser)
    gp.create(rel2)
    for each in extensions:
        rel3 = Relationship(main_tab,"Extension",each)
        gp.create(rel3)
    for each in plugins:
        rel4 = Relationship(main_tab, "Plugin", each)
        gp.create(rel4)
    gp.commit()
    return main_tab, survivors, gp

def draw_graph(gp, main_tab, old_survivors, details, url, duplicate):
    m = [details[x:x+8] for x in range(0, len(details), 8)]  # split the details list into sublist of 8
    new_survivors = []
    for each in m:
        new_survivors.append(each[1])
    print("New survivors are")
    print(new_survivors)
    unique_survivors = [x for x in new_survivors if x not in old_survivors]
    print("Unique new Processes are")
    print(unique_survivors)
    for x in m:
        if x[2] == "renderer":
            new_node = Node("New Tab", name=x[5], PID=x[1], CPU=x[3], Network=x[4], Private_memory=x[6], JSmemory=x[7], URL =url)
            gp.create(new_node)
            connection = Relationship(main_tab, "New Link Opened", new_node)
            gp.create(connection)
    for x in m:
        if x[1] in unique_survivors:
            if x[2] == "plugin":
                plugin_node = Node("Plugin", name=x[5], PID=x[1], CPU=x[3], Network=x[4], Private_memory=x[6], JSmemory=x[7])
                gp.create(plugin_node)
                plugin_rel = Relationship(new_node, "Plugin", plugin_node)
                gp.create(plugin_rel)
            elif x[2] == "extension":
                ext_node = Node("Extension", name=x[5], PID=x[1], CPU=x[3], Network=x[4], Private_memory=x[6], JSmemory=x[7])
                gp.create(ext_node)
                ext_rel = Relationship(new_node, "Extension", ext_node)
                gp.create(ext_rel)
    gp.commit()

graph = Graph("http://localhost:7474/db/data/", user='neo4j', password='cns2202') # connect to the local graph database
graph.delete_all() # Delete all the previous made nodes and relationship
gp = graph.begin()

coordinates = []
coordinates = generate_coordinates(width, height, coordinates)   # generates coordinates based on the diff and the resolution

coordinates=generate_random_coordinates(coordinates)  # already generated coordinates are shuffled randomly

chrome_options = Options()
chrome_options.add_extension("C:\\Users\Deeraj Nagothu\Desktop\Github\Crawler\process_monitor.crx")
# chrome_options.add_extension("C:\\Users\crawler\Desktop\Crawler\process_monitor.crx")

browser=webdriver.Chrome("C:\\Users\Deeraj Nagothu\Desktop\Github\Crawler\chromedriver.exe",chrome_options=chrome_options ) # change this according to the location of the "chromedriver.exe" and chrome options is to add the extension to the chrome as soon as it starts.
# browser=webdriver.Chrome("C:\\Users\crawler\Desktop\Crawler\chromedriver.exe",chrome_options=chrome_options )

browser.get(target)
browser.maximize_window()
main_window = browser.current_window_handle
print("This is my main window : "+str(main_window))
freshly_opened = browser.window_handles
print(freshly_opened)
print(browser.current_window_handle)

initial_details = get_initital_browser_data(1,freshly_opened)
print("printing the initial draw graph details !")
main_tab, survivors, gp = initial_draw_graph(initial_details, gp)
gp = graph.begin()
for coordinate in coordinates:
    clicked=clicker(coordinate)
    sleep(2)
    number_of_tabs = len(browser.window_handles)
    if( number_of_tabs == 1):
        sleep(1)
        continue
    else:
        already_open = browser.window_handles
        details, url, duplicate = get_tab_data(1,already_open)
        draw_graph(gp, main_tab, survivors, details, url, duplicate)
        gp = graph.begin()
        sleep(2)

print("CRAWLING SUCCESSFULLY FINISHED !")