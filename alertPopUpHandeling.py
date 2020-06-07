import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
class Test(unittest.TestCase):
    application_under_test="http://localhost/Automation/PackAndGo_v2/"
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="<path of the driver>")
        self.driver.get(self.application_under_test);
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
    def tearDown(self):
        self.driver.close()
        
  
    def testName(self):
        
        self.driver.find_element_by_link_text("Login").click()
        #Locate and enter the username & password values
        self.driver.find_element_by_id("usernameLogin").send_keys("pgGru")
        self.driver.find_element_by_id("passwordLogin").send_keys("freezeray")
        #click on the login button
        self.driver.find_element_by_id("login").click()
        #select the source of travel
        sourceDropdown=self.driver.find_element_by_id("fromDD")
        select_Source=Select(sourceDropdown)
        select_Source.select_by_value("Bengaluru")
        #select the destination of travel
        destDropdown=self.driver.find_element_by_id("toDD")
        select_Dest=Select(destDropdown)
        select_Dest.select_by_value("Hyderabad")
        #click on search bus button
        self.driver.find_element_by_id("searchBus").click()
        #select the bus slot row
        self.driver.find_element_by_xpath("//*[@id='radio3']").click()
        #click on proceed to booking button
        self.driver.find_element_by_id("book").click()
        
        #Enter no of passengers
        self.driver.find_element_by_id("counter").clear()
        self.driver.find_element_by_id("counter").send_keys("2")
        #click on calculate bill
        self.driver.find_element_by_xpath("//*[@id='rowB6']/td/p/input").click()
        #Click on Confirm button.
        
        self.driver.find_element_by_id("confirmBooking").click()
        
        alert_message = self.driver.switch_to_alert().text
        print(alert_message)
        
        self.driver.switch_to_alert().accept()
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
