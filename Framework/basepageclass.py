from selenium import webdriver
from time import sleep


class BasePageClass:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self.timeout = 30

    def wait_for_element(self, timeout, *element):
        tout = timeout
        current_wait = 0
        while tout > current_wait:

            try:
                el = self.driver.find_element(element[0], element[1])
                el.is_displayed()
                break

            except:
                current_wait += 0.5
                sleep(0.5)

    def wait_for_text(self, timeout, *element):
        tout = timeout
        current_wait = 0
        while tout > current_wait:

            try:
                el = self.driver.find_element(element[0], element[1])
                if el.text != '':
                    break

            except:
                current_wait += 0.5
                sleep(0.5)

    def check_if_element_exists(self,*element):
        self.wait_for_element(30,*element)
        lbl = self.driver.find_element(*element)
        return lbl.is_displayed()

    def return_element_text(self,*element):
        elm = self.check_if_element_exists(*element)
        return elm.text