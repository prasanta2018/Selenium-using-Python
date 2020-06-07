'''
Checkbox Demo
'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
#make necessary imports
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as waitE


driver = webdriver.Chrome("C://Selenium Web Driver//Chrome//chromedriver.exe")
''' Implicit wait'''
driver.implicitly_wait(20)
driver.get("http://the-internet.herokuapp.com/")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='content']/ul/li[6]/a").click()
#time.sleep(5)
'''Explicit Wait'''
# Wait as long as required, or maximum of 10 sec for the table to appear
#visibility_of_element_located- One of the predefined conditions to use with WebDriverWait from the expected_conditions module. 
WebDriverWait(driver,10).until(waitE.visibility_of_element_located((By.ID, 'travelTable')))

driver.find_element_by_xpath("//*[@id='checkboxes']/input[2]").click()


driver.close()