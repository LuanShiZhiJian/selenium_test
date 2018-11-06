import unittest
from selenium import webdriver

#第一种方式直接定义浏览器驱动
class Mytest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

'''
第二种方式：调用浏览器驱动
# from .driver import browser
class Mytest(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
'''