from Framework.basepageclass import BasePageClass
from Locators.LoginPageLocators import LoginPageLocator

class LoginPage(BasePageClass):

    def enter_username(self,username):
        self.wait_for_element(*LoginPageLocator.USERNAME)
        uname = self.driver.find_element(*LoginPageLocator.USERNAME)
        uname.send_keys(username)

    def enter_pass(self,password):
        self.wait_for_element(*LoginPageLocator.USERNAME)
        pword = self.driver.find_element(*LoginPageLocator.PASSWORD)
        pword.send_keys(password)

    def click_login(self):
        self.wait_for_element(*LoginPageLocator.BTNLOGIN)
        btn = self.driver.find_element(*LoginPageLocator.BTNLOGIN)
        btn.click()

    def login_as(self,username,password):
        self.enter_username(username)
        self.enter_pass(password)
        self.click_login()

    def check_if_label_exists(self,*label):
        self.wait_for_text(*label)
        lbl = self.driver.find_element(*label)
        return lbl

    def click_forgot_password(self):
        self.wait_for_element(*LoginPageLocator.FORGOTPASSWORD)
        fp = self.driver.find_element(*LoginPageLocator.FORGOTPASSWORD)
        fp.click()

    def welcome_msg(self):
        self.wait_for_text(*LoginPageLocator.WELCOME)
        welcome = self.driver.find_element(*LoginPageLocator.WELCOME)
        return welcome.text
