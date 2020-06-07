'''
Unit Test Module for Circle Program

'''
from testSuiteDemo.circleProgram import circle
import unittest

#make necessary imports
object1=None

#setUpModule-instantiates the object and returns the same.
def setUpModule():
    object1=circle()
    print("Module")
    return object1

#tearDownModule-uninstantiates the object.
def tearDownModule():
    object1=None

class TestCircle(unittest.TestCase):
    #setupClass- creates a list of test data
    @classmethod
    def setUpClass(cls):
        cls.a=[2,3,10]
    
    def setUp(self):
        print("before test method")
    #test methods    
    def test_1(self):
        print("test1")
        print(setUpModule().circle_area(self.a[0]))
       
    def test_2(self):
        print("test2")
        print(setUpModule().circle_area(self.a[1]))
       
    def test_3(self):
        print("test3")
        print(setUpModule().circle_area(self.a[2]))
       
    def tearDown(self):
        print("after test method ")  
    @classmethod
    def tearDownClass(cls):
        print("in tear down class method")
        

''' Defining the Test Suite '''
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    #get all tests from TestCircle
    tc1=unittest.TestLoader().loadTestsFromTestCase(TestCircle)
    tc2=unittest.TestLoader().loadTestsFromTestCase(TestCircle)
    
    # create a test suite combining tc1 
    test_suite = unittest.TestSuite([tc1,tc1])
    # run the suite
    unittest.TextTestRunner(verbosity=1).run(test_suite)

''' NOTE: 
Observation-1: If we load same test module multiple times in a TestLoader, 
            it only excutes once for duplicate test module.

'''
     
        