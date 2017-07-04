from Framework.basepageclass import BasePageClass
from Locators.ForgotPasswordLocators import ForgotPasswordLocator

class ForgotPasswordPage(BasePageClass):

    def click_back_to_login(self):
        self.wait_for_element(*ForgotPasswordLocator.RETURNTOLOGIN)
        backtologin = self.driver.find_element(*ForgotPasswordLocator.RETURNTOLOGIN)
        backtologin.click()

    def enter_email(self,email):
        self.wait_for_element(*ForgotPasswordLocator.ENTEREMAIL)
        enteremail = self.driver.find_element(*ForgotPasswordLocator.ENTEREMAIL)
        enteremail.send_keys(email)

    def click_request_new_pass_btn(self):
        self.wait_for_element(*ForgotPasswordLocator.BTNREQUESTNEWPASSWORD)
        btn = self.driver.find_element(*ForgotPasswordLocator.BTNREQUESTNEWPASSWORD)
        btn.click()

    def element_text(self,*element):
        self.wait_for_text(element[0],element[1])
        elm = self.driver.find_element(element[0],element[1])
        return elm.text

