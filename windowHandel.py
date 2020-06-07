import unittest
from selenium import webdriver
class Test(unittest.TestCase):
    application_under_test = "http://localhost:84/Common/Login.aspx"
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="<path of the driver>")
        self.driver.get(self.application_under_test);
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()
    def testName(self):
        self.driver.find_element_by_link_text("About Us").click()
        
        wind_handle = self.driver.window_handles
        
        print(len(wind_handle))
        
        for i in wind_handle:
            self.driver.switch_to_window(i)
            print(self.driver.current_url)
            
        paragraph1 = self.driver.find_element_by_xpath("/html/body/form/div[3]/div[3]/p[1]").text
    
        print("About us details: ",paragraph1)
     
if __name__ == "__main__":
    unittest.main()
