from selenium import webdriver
from selenium.webdriver.support.ui import Select
browser=webdriver.Chrome(<<Path of the chrome browser driver>>)
browser.get("http://localhost/Automation/PackAndGo_v2/")
#click on the login link
browser.find_element_by_link_text("Login").click()
#Locate and enter the username & password values
browser.find_element_by_id("usernameLogin").send_keys("pgGru")
browser.find_element_by_id("passwordLogin").send_keys("freezeray")
#click on the login button
browser.find_element_by_id("login").click()
#select the source of travel
sourceDropdown=browser.find_element_by_id("fromDD")
select_Source=Select(sourceDropdown)
select_Source.select_by_value("Bengaluru")
#select the destination of travel
destDropdown=browser.find_element_by_id("toDD")
select_Dest=Select(destDropdown)
select_Dest.select_by_value("Hyderabad")
#click on search bus button
browser.find_element_by_id("searchBus").click()
#select the bus slot row
browser.find_element_by_xpath("//*[@id='radio3']").click()
#click on proceed to booking button
browser.find_element_by_id("book").click()
