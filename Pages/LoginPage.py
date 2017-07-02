from Framework.basepageclass import BasePageClass
from Locators.LoginPageLocators import LoginPageLocator

class LoginPage(BasePageClass):

    def enter_username(self,username):
        self.wait_for_element(30,*LoginPageLocator.USERNAME)
        uname = self.driver.find_element(*LoginPageLocator.USERNAME)
        uname.send_keys(username)

    def enter_pass(self,password):
        self.wait_for_element(30,*LoginPageLocator.USERNAME)
        pword = self.driver.find_element(*LoginPageLocator.PASSWORD)
        pword.send_keys(password)

    def click_login(self):
        self.wait_for_element(30,*LoginPageLocator.BTNLOGIN)
        btn = self.driver.find_element(*LoginPageLocator.BTNLOGIN)
        btn.click()

    def login_as(self,username,password):
        self.enter_username(username)
        self.enter_pass(password)
        self.click_login()

    def check_if_label_exists(self,*label):
        self.wait_for_element(30,*label)
        lbl = self.driver.find_element(*label)
        return lbl

    def click_forgot_password(self):
        self.wait_for_element(30,*LoginPageLocator.FORGOTPASSWORD)
        fp = self.driver.find_element(*LoginPageLocator.FORGOTPASSWORD)
        fp.click()

