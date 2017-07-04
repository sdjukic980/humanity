from time import sleep
import unittest
from selenium import webdriver


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass


    @classmethod
    def tearDownClass(cls):
        pass



    def setUp(self):
        self.driver = webdriver.Chrome("C:\\humanity\\chromedriver.exe")
        self.driver.maximize_window()
        base_url = "https://automation1.humanity.com/app/"
        self.driver.get(base_url)

    def tearDown(self):
        self.driver.quit()