from selenium import webdriver
from select import select
from selenium.webdriver.support.ui import Select
import unittest
import time
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys


class Submit(unittest.TestCase):
    
    app_under_test = "https://www.netflix.com/in/"
    titleList = []

    # test setup
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C://Selenium Web Driver//Chrome//chromedriver.exe")

        # implicit wait
        self.driver.implicitly_wait(10)
        self.driver.get(self.app_under_test)
        
        # title of the page
        print(self.driver.title)
        
        # maximize
        self.driver.maximize_window()
        
        # take screenshot
        self.driver.get_screenshot_as_file("C://Users//pmanda1x//Desktop//MP//init.png")
    
    
    # test action
    
    def testName(self):

        self.driver.find_element_by_link_text("Sign In").click()
        try:
            self.driver.find_element_by_id("id_userLoginId").send_keys('wooedotin112@gmail.com')
        except Exception as e:
            print("Exception:",e)
        self.driver.find_element_by_id("id_password").send_keys("netflix002")
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@id='appMountPoint']/div/div[3]/div/div/div[1]/form/button").click()
        time.sleep(5)
        
        self.driver.find_element_by_xpath("//*[@id='appMountPoint']/div/div/div[1]/div[1]/div[2]/div/div/ul/li[3]/div/a/div/div").click()
        time.sleep(5)

        # working with table
        #self.driver.get("https://www.geeksforgeeks.org/difference-between-ram-and-rom/")
        self.driver.get("https://chercher.tech/practice/table")
        table = self.driver.find_element_by_xpath("//*[@id='webtable']")
        rows= table.find_elements_by_tag_name("tr")
        time.sleep(3)
        length = len(rows)
        #print("Rows=",length)
        
        for i in range(0,length):          
            columns = rows[i].find_elements_by_tag_name("td")
            #print("i=" , i)
            #print("Row text:",rows[i].text)
            #print("Columns=", len(columns))       
            
            if (i==0):
                txt = rows[i].text
                print(txt)
                self.titleList = list(txt.split(" "))
                #print("titleList length:",len(self.titleList))

            for j in range(0,len(columns)):
                #print("j=" , j)
                #print(len(self.titleList))
                print(self.titleList[j] + ":" + columns[j].text)
        
        
        print("Number of Rows in Table",length-1)
        # assertion check
        self.assertEqual(length-1,4)
    # test tear down
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

'''
driver.refresh()
driver.forward()

driver.get("https://www.google.com")
driver.refresh()
windows = driver.window_handles
print(str(len(windows)) + "," + driver.current_url)


driver.back()

windows = driver.window_handles
print(str(len(windows)) + "," + driver.current_url)


#---------------------------------------------
driver.refresh()
#driver.forward()
# Click on sign in
driver.find_element_by_link_text("Sign In").click()
driver.find_element_by_id("id_userLoginId").send_keys('wooedotin112@gmail.com')
driver.find_element_by_id("id_password").send_keys("netflix002")
driver.find_element_by_xpath("//*[@id=appMountPoint']/div/div[3]/div/div/div[1]/form/button").click()
#*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button
print(driver.title)
print(driver.current_url)
driver.get_screenshot_as_file("C://Users//pmanda1x//Desktop//MP//netflix.png")
#print(screenshotBinaryData)
driver.get("http://www.google.com")
#Get Page Source Property
pageProperty=driver.page_source
if "google" in pageProperty:
    print("Found")
else:
    print("Not found")
#print(pageProperty)
driver.get_screenshot_as_file("google.png")
driver.back()
#driver.quit()
driver.close()



toMmt = driver.find_element_by_id("FromCity")
droptoMmt = Select(toMmt)
droptoMmt.select_by_value("Bangalore, India")

driver.find_element_by_name("Search").click()


'''




