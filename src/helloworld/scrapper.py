from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import xml.etree.ElementTree as ET

def scrapper():
    """""""""""Student Info"""""""""""
    # We read it in the xml file:
    options_path = os.path.dirname(os.path.abspath(__file__)) + "/resources/student_options.xml"
    tree = ET.parse(options_path)
    root = tree.getroot()

    student_language = root.find("language").text
    student_level = root.find("level").text
    student_UE3_1 = root.find("UE3_1").text
    student_UE3_2 = root.find("UE3_2").text

    ##################################

    DRIVER_PATH = os.path.dirname(os.path.abspath(__file__)) + '/chromedriver'
    SCREENSHOTS_PATH = os.path.dirname(os.path.abspath(__file__)) + '/resources/edt/'

    options = Options()
    options.headless = True    # flag to decide if the page is displayed (False) or not (True)
    options.add_argument("--window-size=1920,1200")

    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get("https://planning.inalco.fr/public")

    delay = 3 # timeout delay in seconds

    #WEBPAGE
    try: # wait for the page to load
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'GInterface.Instances[1].Instances[1].bouton_Edit')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading of page took too much time!")

    #MAIN PLANNING
    driver.find_element(By.ID, "GInterface.Instances[1].Instances[1].bouton_Edit").send_keys(student_language + " " + student_level)
    driver.find_element(By.ID, "GInterface.Instances[1].Instances[1].bouton_Edit").send_keys(Keys.RETURN)

    try: # wait for the table to load
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'GInterface.Instances[1].Instances[7]')))
        print("Table is ready!")
    except TimeoutException:
        print("Loading of table took too much time!")

    edt = driver.find_element(By.ID, "GInterface.Instances[1].Instances[7]")
    edt.screenshot(SCREENSHOTS_PATH + student_language + student_level + "_edt.png")
    print("=> Main planning saved")

    #SWITCH TO "MATIERES" SECTION
    driver.find_element(By.ID, "GInterface.Instances[0].Instances[1]_Combo2").click()
    driver.find_element(By.ID, "GInterface.Instances[1].Instances[0].bouton_Edit").click()
    time.sleep(0.5)
    driver.find_element(By.ID, "GInterface.Instances[1].Instances[0]_Liste").send_keys(Keys.ARROW_DOWN)
    driver.find_element(By.ID, "GInterface.Instances[1].Instances[0]_Liste").send_keys(Keys.RETURN)


    #LOAD UE3 PLANNINGS
    try: # wait for the table to load
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'GInterface.Instances[1].Instances[1].bouton_Edit')))
        print("Matieres section is ready!")
    except TimeoutException:
        print("Loading of matieres section took too much time!")

    #FIRST UE3
    driver.find_element(By.ID, "GInterface.Instances[1].Instances[1].bouton_Edit").send_keys(student_UE3_1)
    driver.find_element(By.ID, "GInterface.Instances[1].Instances[1].bouton_Edit").send_keys(Keys.RETURN)
    try: # wait for the ue3_1 to load
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'GInterface.Instances[1].Instances[7]')))
        print("First UE3 is ready!")
    except TimeoutException:
        print("Loading of first UE3 took too much time!")
    edt_ue3_1 = driver.find_element(By.ID, "GInterface.Instances[1].Instances[7]")
    time.sleep(0.5)
    edt_ue3_1.screenshot(SCREENSHOTS_PATH + student_UE3_1 + "_edt.png")
    print("=> First UE3 planning saved")

    #SECOND UE3
    driver.find_element(By.ID, "GInterface.Instances[1].Instances[1].bouton_Edit").clear()
    driver.find_element(By.ID, "GInterface.Instances[1].Instances[1].bouton_Edit").send_keys(student_UE3_2)
    driver.find_element(By.ID, "GInterface.Instances[1].Instances[1].bouton_Edit").send_keys(Keys.RETURN)
    try: # wait for the ue3_1 to load
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'GInterface.Instances[1].Instances[7]')))
        print("Second UE3 is ready!")
    except TimeoutException:
        print("Loading of second UE3 took too much time!")
    edt_ue3_2 = driver.find_element(By.ID, "GInterface.Instances[1].Instances[7]")
    time.sleep(0.5)
    edt_ue3_2.screenshot(SCREENSHOTS_PATH + student_UE3_2 + "_edt.png")
    print("=> Second UE3 planning saved")


    ########################
    if not options.headless:
        time.sleep(3)
    driver.quit()
    print("Page closed.")