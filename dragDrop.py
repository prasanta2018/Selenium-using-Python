import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
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
        self.driver.find_element_by_link_text("Drag 'N' Drop").click();
        source = self.driver.find_element_by_id("draggable")
        target = self.driver.find_element_by_id("droppable")
        mouse = ActionChains(self.driver).drag_and_drop(source, target)
        mouse.perform()
        
        msg_after_drop = self.driver.find_element_by_xpath("//*[@id='droppable']/p").text
        
        assert "Dropped!" in msg_after_drop
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
