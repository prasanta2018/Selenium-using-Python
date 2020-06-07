'''
Radio Button
'''

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome("C://Selenium Web Driver//Chrome//chromedriver.exe")

driver.get("https://paytm.com/train-tickets")

driver.maximize_window()

time.sleep(2)

radioButton = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/div/div[3]/label")
driver.find_el
radioButton.click()


selectionState = radioButton.is_selected()
print(selectionState)
'''
if( selectionState == "False" ):
    radioButton.click()
'''
time.sleep(5)
driver.close()