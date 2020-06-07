import unittest
from selenium import webdriver
import xlrd
import time
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
        WorkBook = xlrd.open_workbook("Pack_Go.xlsx")        
        WorkSheet = WorkBook.sheet_by_index(0)
        RowCount = WorkSheet.nrows       
        
        for i in range(1,RowCount):
            Username =  WorkSheet.cell_value(i,0)
            Password = WorkSheet.cell_value(i,1)
            self.driver.find_element_by_link_text("Login").click()
            self.driver.find_element_by_id("usernameLogin").send_keys(Username)
            self.driver.find_element_by_id("passwordLogin").send_keys(Password)
            self.driver.find_element_by_id("login").click()
            self.driver.find_element_by_link_text("LogOut").click()
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
