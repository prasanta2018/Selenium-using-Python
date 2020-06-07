import unittest
from selenium import webdriver
import xlwt
import xlrd
import time
from xlutils.copy import copy
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
        filepath = "Pack_Go.xlsx";
        WorkBook = xlrd.open_workbook(filepath)
        writebook = copy(WorkBook)
        sheet = WorkBook.sheet_by_index(0)
        writesheet = writebook.get_sheet(0)
        RowCount = sheet.nrows
        
        for i in range(1,RowCount):
            Username =  sheet.cell_value(i,1)
            Password = sheet.cell_value(i,2)
            time.sleep(3)
            self.driver.find_element_by_link_text("Login").click()
            self.driver.find_element_by_id("usernameLogin").send_keys(Username)
            self.driver.find_element_by_id("passwordLogin").send_keys(Password)
            time.sleep(2)
            self.driver.find_element_by_id("login").click()
            if(self.driver.title=="Dashboard"):
                writesheet.write(i,3,"LoginSuccess")    
                self.driver.find_element_by_link_text("LogOut").click()
                if(sheet.cell_value(i,0)=="valid"):
                    writesheet.write(i,4,"Pass")
                else:
                    writesheet.write(i,4,"fail")  
                    
            else:
                writesheet.write(i,3,"Loginfailed")
                self.driver.find_element_by_id("closeLogin").click()
                if(sheet.cell_value(i,0)=="invalid"):
                    writesheet.write(i,4,"Pass")
                else:
                    writesheet.write(i,4,"fail")       
            
        writebook.save(filepath)
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
