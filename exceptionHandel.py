import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotInteractableException
class Test(unittest.TestCase):
    application_under_test="http://localhost/Automation/PackAndGo_v2/"
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="<path of the driver>")
        self.driver.get(self.application_under_test);
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
    def tearDown(self):
        self.driver.quit()
    def testName(self):
        try:
            self.driver.find_element_by_link_text("Login").click()
        #Locate and enter the username & password values
            self.driver.find_element_by_id("usernameLogin").send_keys("pgGru")
            self.driver.find_element_by_id("passwordLogin").send_keys("freezeray")
        #click on the login button
            self.driver.find_element_by_id("login").click()
            
            self.driver.find_element_by_xpath("//*[@id='sideMenu3']").click()
            self.driver.find_element_by_id("clearAccount").click()
            self.driver.find_element_by_link_text("LogOut").click()
        except NoSuchElementException as ne:
            print(ne)
        except ElementNotInteractableException as ei:
            print(ei)
        except Exception as e:
            print(e)
        finally:
            self.driver.close()
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
