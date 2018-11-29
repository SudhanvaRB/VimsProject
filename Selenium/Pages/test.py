from selenium import webdriver
import time
import unittest
from test_login import Login
from test_homepage import homepage
from selenium.webdriver import ActionChains
import pyautogui

class Flip(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(Flip, cls).setUpClass()
        cls.driver = webdriver.Chrome("C:\selenium_scripts\Selenium\driver\chromedriver.exe")
        #cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

        
    def test_login(self):
        driver = self.driver
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.dashboard_appointments()#added comment  for storing in git
#=====================================
        
       
        
    
    @classmethod
    def tearDownClass(cls):
        super(Flip, cls).tearDownClass()
        cls.driver.close()
        cls.driver.quit()
        


