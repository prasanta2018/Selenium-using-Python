from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
#instantiate the driver instance
driver = webdriver.Chrome(executable_path="<Path of the driver>")
#launch the application
driver.get("http://localhost/Automation/PackAndGo_v2/")
#maximize the window
driver.maximize_window()
print(driver.title)
#click on the offers link
driver.find_element_by_link_text("Offers").click();
#locating the table element as in <table> tag.
table = driver.find_element_by_id("offersTable")
#locating the rows in the table as in <tr> tags within the <table> tag
rows = table.find_elements_by_tag_name("tr")
time.sleep(3)
print(len(rows))
#iterating through the list of rows
for i in range(0,len(rows)):
    print(rows[i].text)
    if(i!=0):
        #locating the columns the each row as in <td> tags within the <tr> tag   
        cols=rows[i].find_elements_by_tag_name("td")
        for j in cols:
            print(j.text)
 
#close the table
driver.find_element_by_id("crossTable").click()
driver.save_screenshot("pack.png")
#close the browser              
driver.close()
