from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


#setting up
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
actions = ActionChains(driver)

driver.get('https://www.pokemon-planet.com')
#activate Flash. (Flash was turned off by default so need to do this first.)
driver.get("chrome://settings/content/siteDetails?site=https%3A%2F%2Fpokemon-planet.com")
actions = ActionChains(driver)
actions = actions.send_keys(Keys.TAB * 21) # number of tabs can vary
actions = actions.send_keys(Keys.SPACE)
actions = actions.send_keys("a")
actions = actions.send_keys(Keys.ENTER)
actions.perform()

#Going to website and logging in

driver.back()
time.sleep(1)
#ids are found in the html. Right click a webpage and "inspect element"
play_now = driver.find_element_by_id("playnow2")
play_now.click()
username = driver.find_element_by_id("user")
username.send_keys() # Enter username inside paranthesis
password = driver.find_element_by_id("passwrd")
password.send_keys() # Enter password inside paranthesis
password.send_keys(Keys.RETURN)
time.sleep(2)

playNow = driver.find_element_by_id("playnowbutton")
playNow.click()
actions.perform()
