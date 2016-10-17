# Author: Deeraj Nagothu, MS in ECE @Binghamton University
# Internet Crawler
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
width, height = pyautogui.size()  # get the resolution of the screen. Changes according to the system used
pyautogui.FAILSAFE = False
t = 75  # set a threshold value for origin points to click
target = 'https://www.ebay.com' # taget website to crawl

def html_get_value(html_line):  # get value from a html line. Like "<span class="th" jscontent="pid" jstcache="12">3944</span>" will return 3944
    x = list(html_line)
    if len(x)==0:
        return "Nothing"
    else:
        return x[0]

def get_tab_data(flag, already_open):  #  open the new tab for memory data and get data
    if flag == 1:
        duplicate = 0 # declaring the default value for tab having similar PID detection
        print("Entered the get tab data function")
        pyautogui.keyDown('ctrlleft')      # ctrl+T combination to open new tab in the browser
        pyautogui.keyDown('t')
        pyautogui.keyUp('t')
        pyautogui.keyUp('ctrlleft')
        handle = browser.window_handles  # gives the list of handles in the browser representing each tab
        newly_opened_tab_handle = [x for x in handle if x not in already_open]  # this gives the window handle which was opened as new tab.
        browser.switch_to_window(newly_opened_tab_handle[0])  # moves the focus to new tab
        # The below link changes with the browser.
        # This can be obtained using the inspect element option in the extension
        # This is generally just an extension popup, but opened as a new page in new tab so that
        # it can be downloaded and parsed.
        browser.get('chrome-extension://eobmgbdhncfblmillcdjjnnbhcpjognj/popup.html')
        sleep(3)
        pyautogui.keyDown('shift')  # Shift+ESC option in chrome opens the task manager
        pyautogui.press('esc')
        pyautogui.keyUp('shift')
        x = pyautogui.size()  # Getting the size of the screen
        # The task manager pops ip in the center of the screen. The Javascript Memory by default is not active.
        # We need to make it active using the task manager option in right click.
        #  Below the center of the screen is computed
        # Those co-ordinates (y,z) is used to make a right click and make Javascript memory active.
        y = int(x[0]/2)
        z = int(x[1]/2)
        pyautogui.click(y, z, button='right' )
        pyautogui.press('up') # Used to select the Javascript memory from the menu
        pyautogui.press('up')
      # pyautogui.press('up')
        pyautogui.press('enter')
        sleep(2)
        html = browser.page_source # get the page source to parse
        soup = BeautifulSoup(html, "html.parser") # Parser used to get the data from the page

        pyautogui.press('esc')
        table = soup.find_all("tr") # The relevant data required is in a tabular column
        details = [] # List to save all the data from the current browser state.
        # The data collected is available from the extension used. The data is appended to the list created
        # The type f data collected is local PID in chrome browser, system PID, Type of process, CPU consumption,
        # network consumption, Title of the tab, Private tab memory and the Javascript memory
        # The system PID is used to collect other relevant information about the tab process created.
        # Google chrome uses instantiates different process for each tab created.
        for each in range(1, len(table)):
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
            # The new tab can have a unique process or use the same PID as the main tab. If it is using the same as
            # main tab, then the tiles of both main tab and new tab are in the same list. The below parameter "q"
            # records the titles in list, and later this can be used to detect the duplication of PID by new tab.

            q = [i for i in range(len(text)) if text.startswith("title", i)]
            print("the position is"+str(q))
            if len(q) > 1:                              # sometimes the new tab uses the same PID as the parent tab.
                title = text[q[1]+8:len(text)-3]        # Whenever it does that, the child node is created with the same
                duplicate = 1                           # PID as the parent. The "duplicate" parameter is used to
            else:                                       # detect if the particular new tab has a unique PID or it is
                title = text[q[0]+8:len(text)-3]        # using the same as main tab PID.

            print("The final title is "+str(title))
            details.append(title)

            print("Private Memory is "+x[6].get_text())
            details.append(x[6].get_text())
            print("JavaScript Memory is "+x[7].get_text())
            details.append(x[7].get_text())

    sleep(3)
  # browser.find_element_by_tag_name("body").send_keys(Keys.CONTROL + "w") # close the memory tab along with the newly opened tab.
    pyautogui.keyDown('ctrlleft') # CTRL+W is used to close the current focus tab which is extension popup
    pyautogui.keyDown('w')
    pyautogui.keyUp('w')
    pyautogui.keyUp('ctrlleft')
    sleep(2)
    browser.switch_to_window(already_open[0]) # The focus is required to be changed after the previous tab is closed
# The list already_open consists of handles which where available before opening the tab which was closed here
# The lists first element consists of the main browser initial tab. Here the focus was shifted to main tab.
# The newly opened tab is still open. We have to close the new tab to proceed with the next link.

    pyautogui.keyDown('ctrlleft') # Change the tab to the new tab opened on click
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyUp('ctrlleft')
    sleep(1)
    print("The window handle after TAB is : "+str(browser.current_window_handle))
    check_tabs = browser.window_handles
    # Check to make sure that it is going to close the new tab instead of main tab.
    # Checking will be done based on the window handles because we know the main handle.
    for tab_num in range(len(check_tabs)-1, 0, -1):
        print("The tab going to be closed is : "+str(check_tabs[tab_num]))
        sleep(2)
        browser.switch_to_window(check_tabs[tab_num])
        print("The current window handle is : "+str(browser.current_window_handle))
        sleep(1)
        url = browser.current_url # Saving the url of the newly opened tab
        print("#################################################################################################")
        print("THis is the URL of this page : "+str(url))
        sleep(1)
        # Closing the tab after making sure about the handle which is going to be closed
        pyautogui.keyDown('ctrlleft')
        pyautogui.keyDown('w')
        pyautogui.keyUp('w')
        pyautogui.keyUp('ctrlleft')
        sleep(2)
        print("Tab was closed an the remaining tabs are "+str(browser.window_handles))
        sleep(2)


    browser.switch_to_window(already_open[0]) # Switching back to the main tab.
    # Now at this point there should be only one tab opened which is main default tab.
    print("Switched to the main handle")
    sleep(3)
    return details, url, duplicate
# The following function has the same functionality as the above function. The below function is used to get the data
# when the browser is started. This provides the initial information about the browser.
# The separate function is made because the above function is triggered when a new tab opened was deteceted.
# But in the initial case there wont be any new tab opened. That's why a new function was required.
# The below function consists of the same feature except that there wont be a newly opened link to close.
def get_initital_browser_data(flag,freshly_opened):
    if flag == 1:
        pyautogui.keyDown('ctrlleft')
        pyautogui.keyDown('t')
        pyautogui.keyUp('t')
        pyautogui.keyUp('ctrlleft')
        handle = browser.window_handles
        print(handle)
        newly_opened_tab_handle = [x for x in handle if x not in freshly_opened]
        print(newly_opened_tab_handle)
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
    pyautogui.keyDown('ctrlleft')
    pyautogui.keyDown('w')
    pyautogui.keyUp('w')
    pyautogui.keyUp('ctrlleft')
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
        for j in range(75, height, difference): # 75 and 100 are used like a threshold difference which can change
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
    coordinates = temp_coordinates
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
    pyautogui.moveTo(x[0], x[1], duration=0.1) # This duration specifies how speed the mouse travels
    pyautogui.click(x[0], x[1])
    pyautogui.keyUp('ctrlleft')
    return True

# This function is called when there is data collected about the initial status of the browser
def initial_draw_graph(details, gp):
    m = [details[x:x+8] for x in range(0, len(details), 8)] # split the details list into sublist of 8
# Categorized such that each of them can be made as nodes and then later relationships can be established
    extensions = []
    plugins = []
    survivors = []
    # The following part is to create the Nodes
    for x in m:
        if x[2] == "browser":
            print("the browser list is:")
            print(x)
            # This feeds the info into the Node
            browser = Node("Browser", name=x[5], PID=x[1], CPU=x[3], Network=x[4], Private_memory=x[6], JSmemory=x[7])
            gp.create(browser)  # creates the Node with the data
            survivors.append(x[1]) # appends the current PID to the survivors list
        elif x[2] == "gpu":
            print("the gpu list is")
            print(x)
            gpu = Node("GPU", name=x[5], PID=x[1], CPU=x[3], Network=x[4], Private_memory=x[6], JSmemory=x[7])
            gp.create(gpu)
            survivors.append(x[1])
        elif x[2] == "extension":
            print("the extension list is")
            print(x)
            node = Node("iExtension", name=x[5], PID=x[1], CPU=x[3], Network=x[4], Private_memory=x[6], JSmemory=x[7])
            gp.create(node)
            extensions.append(node)
            if x[5] != "Extension: chrome-extension://eobmgbdhncfblmillcdjjnnbhcpjognj/popup.html":
                survivors.append(x[1])
        elif x[2] == "renderer":
            print("the renderer list is")
            print(x)
            main_tab = Node("Main_Tab", name=x[5], PID=x[1], CPU=x[3], Network=x[4], Private_memory=x[6], JSmemory=x[7])
            main_tab_pid = x[1]
            gp.create(main_tab)
            survivors.append(x[1])
        elif x[2] == "plugin":
            print("the plugin list is")
            print(x)
            node = Node("iPlugin", name=x[5], PID=x[1], CPU=x[3], Network=x[4], Private_memory=x[6], JSmemory=x[7])
            gp.create(node)
            plugins.append(node)
            survivors.append(x[1])
    # The following part is to create the relationship between the browser initial stage
    rel1 = Relationship(main_tab,"GPU",gpu)
    gp.create(rel1)
    rel2 = Relationship(main_tab,"Browser",browser)
    gp.create(rel2)
    for each in extensions:
        rel3 = Relationship(main_tab,"Initial Extension",each)
        gp.create(rel3)
    for each in plugins:
        rel4 = Relationship(main_tab, "Initial Plugin", each)
        gp.create(rel4)
    gp.commit() # Commit writes the changes made to the database
    return main_tab, survivors, gp, main_tab_pid
# The main tab pid is required because everytime there is a new tab opened the initial details of the main tab are
# re-recorded as a new node. There are new nodes with the same url. Using this as reference there wont be any
# new node with the same PID created.

# The following function has the same functionality as above, but this is used when there is a new tab opened
def draw_graph(gp, main_tab, old_survivors, details, url, duplicate, main_tab_pid):
    m = [details[x:x+8] for x in range(0, len(details), 8)]  # split the details list into sublist of 8
    new_survivors = []
    for each in m:
        new_survivors.append(each[1])
    print("New survivors are")
    print(new_survivors)
    unique_survivors = [x for x in new_survivors if x not in old_survivors]
    print("Unique new Processes are")
    print(unique_survivors)
    print("the main tab PID is ", main_tab_pid)
    print("Duplication is ", duplicate)
    for x in m:
        if x[2] == "renderer" and x[1] == main_tab_pid and duplicate == 1:
            # comparing so that there is no duplicate of the main tab
            # the duplicate parameter makes sure that the child tab with same pid as parent is created.
            new_node = Node("New_Tab", name=x[5], PID=x[1], CPU=x[3], Network=x[4], Private_memory=x[6], JSmemory=x[7], URL =url)
            print(new_node)
            print("printing url again")
            print(url)
            gp.create(new_node)
            connection = Relationship(main_tab, "New Link Opened", new_node)
            gp.create(connection)
        if x[2] == "renderer" and x[1] != main_tab_pid: # comparing so that there is no duplicate of the main tab
            new_node = Node("New_Tab", name=x[5], PID=x[1], CPU=x[3], Network=x[4], Private_memory=x[6], JSmemory=x[7], URL =url)
            print(new_node)
            print("printing url again")
            print(url)
            gp.create(new_node)
            connection = Relationship(main_tab, "New Link Opened", new_node)
            gp.create(connection)
    for x in m:
        if x[1] in unique_survivors and new_node is not None:
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

coordinates = [] # create the list for coordinates
coordinates = generate_coordinates(width, height, coordinates)   # generates coordinates based on the diff and the resolution

coordinates = generate_random_coordinates(coordinates)  # already generated coordinates are shuffled randomly

chrome_options = Options()
chrome_options.add_extension(".\process_monitor.crx") # Adding the extension to chrome
# chrome_options.add_extension("C:\\Users\crawler\Desktop\Crawler\process_monitor.crx")
chromium_path = ".\chrome-win32\chrome.exe" # Use the portable chromium browser
# If chromium browser is not required then by removing the above chromium path, it will start using the default one
# The default will be developer google chrome.
# ONly Dev channel google chrome can support the extension used here. This extension used a particular API.
# The API used is "chrome.processes" and it is available only in the chrome dev-channel and chromium browser
chrome_options.binary_location = chromium_path

browser=webdriver.Chrome(".\chromedriver.exe", chrome_options=chrome_options )
# chrome options is to add the extension to the chrome as soon as it starts.

browser.get(target) # This open the target website
browser.maximize_window() # By default the window is not maximised. This maximises the window
main_window = browser.current_window_handle # Get the main handle for the target website tab
print("This is my main window : "+str(main_window))
freshly_opened = browser.window_handles # Get all the handles
print(freshly_opened)
print(browser.current_window_handle)
# Start Crawling
initial_details = get_initital_browser_data(1,freshly_opened)
print("printing the initial draw graph details !")

main_tab, survivors, gp, main_tab_pid = initial_draw_graph(initial_details, gp) # Makes the initial Node for main tab
gp = graph.begin()
maintab_url = browser.current_url # comparing if the crawler target is still the same else was there any change

# Each coordinate is sent in loop and crawled
for coordinate in coordinates:
    check_main_url = browser.current_url

    if check_main_url == maintab_url: # If the target is still not same then it will reload again and crawl resumes
        clicked = clicker(coordinate)
    else:
        browser.get(target)
        continue
    sleep(2)
    number_of_tabs = len(browser.window_handles)
    if( number_of_tabs == 1):
        sleep(1)
        continue
    else:
        already_open = browser.window_handles
        details, url, duplicate = get_tab_data(1, already_open)
        draw_graph(gp, main_tab, survivors, details, url, duplicate, main_tab_pid) # adds the nodes to the main node created
        gp = graph.begin()
        sleep(2)

print("CRAWLING SUCCESSFULLY FINISHED !")
