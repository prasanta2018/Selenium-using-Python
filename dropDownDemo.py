'''
Drop Down Demo
'''

from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("C://Selenium Web Driver//Chrome//chromedriver.exe")

driver.get("http://the-internet.herokuapp.com/")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='content']/ul/li[11]/a").click()

findDropDownObj = driver.find_element_by_id("dropdown")

dropDownObj = Select(findDropDownObj)

dropDownObj.select_by_visible_text("Option 2")

currentSelection = dropDownObj.first_selected_option
print(currentSelection.text)

''' Find out the drop down options'''
options_list = dropDownObj.options

#A check on the size of the list.
print(len(options_list))
''' Print all the options '''
for option in options_list:
    print(option.text)

''' returns true if the drop down enables multiple options to be selected '''
print(dropDownObj.is_multiple)
#dropDownObj.deselect_by_visible_text("Option 2")

''' Order of quit() and close(): close()--> quit() '''

try:
   
    driver.quit()
    driver.close()
except Exception as e:
    print("Exceptin Occured:", e)


    
    