import unittest
from selenium import webdriver
class Test(unittest.TestCase):
    application_under_test="http://localhost/Automation/DemoApps/PopupBox.aspx"
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="<path of the driver>")
        self.driver.get(self.application_under_test);
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
    def tearDown(self):
        self.driver.close()
    def testName(self):
        self.driver.find_element_by_link_text("Frames").click()        
        self.driver.switch_to_frame("center")        
        text_center = self.driver.find_element_by_xpath("//*[@id='form1']/div[3]/div[2]/div/span").text
        print(text_center)
        assert "Infosys Mysore - GEC2 - Library" in text_center
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
