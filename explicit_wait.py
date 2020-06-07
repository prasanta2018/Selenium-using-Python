'''
Created on May 4, 2020

@author: pmanda1x
'''
from selenium.webdriver.support import expected_conditions as waitE
from selenium import webdriver
# Wait as long as required, or maximum of 10 sec for the table to appear
#visibility_of_element_located- One of the predefined conditions to use with WebDriverWait from the expected_conditions module. 
WebDriverWait(driver,10).until(waitE.visibility_of_element_located((By.ID, 'travelTable')))


#print the current url of the page
print(browser.current_url)