import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
class Test(unittest.TestCase):
    application_under_test="http://10.67.89.41/Automation/HMS/LoginPage.aspx"
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\kiruthika.k02\\Desktop\\chromedriver.exe")
        self.driver.get(self.application_under_test);
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
    def tearDown(self):
        self.driver.close()
    def testName(self):
        self.driver.find_element_by_id("txtUserID").send_keys("11")
        self.driver.find_element_by_id("txtPassword").send_keys("priya")
        self.driver.find_element_by_name("btnLogin").click()
           
        first = self.driver.find_element_by_xpath("//*[@id=\"NavigationMenu\"]/ul/li[3]/a");
        second = self.driver.find_element_by_xpath("//*[@id=\"NavigationMenu:submenu:8\"]/li[3]/a");
        actions = ActionChains(self.driver)
        actions.move_to_element(first)
        actions.click(second)
        actions.perform()
        
        self.driver.find_element_by_link_text("logout").click()
if __name__ == "__main__":
    unittest.main()
