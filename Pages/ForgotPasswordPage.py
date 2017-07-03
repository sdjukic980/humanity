from Framework.basepageclass import BasePageClass
from Locators.ForgotPasswordLocators import ForgotPasswordLocator

class ForgotPasswordPage(BasePageClass):

    def click_back_to_login(self):
        self.wait_for_element(30,*ForgotPasswordLocator.RETURNTOLOGIN)
        backtologin = self.driver.find_element(*ForgotPasswordLocator.RETURNTOLOGIN)
        backtologin.click()

    def enter_email(self,email):
        self.wait_for_element(30,*ForgotPasswordLocator.ENTEREMAIL)
        enteremail = self.driver.find_element(*ForgotPasswordLocator.ENTEREMAIL)
        enteremail.send_keys(email)

    def click_request_new_pass_btn(self):
        self.wait_for_element(30,*ForgotPasswordLocator.BTNREQUESTNEWPASSWORD)
        btn = self.driver.find_element(*ForgotPasswordLocator.BTNREQUESTNEWPASSWORD)
        btn.click()

    def error_label_text(self):
        self.wait_for_text(self.timeout,*ForgotPasswordLocator.LABELERROR)
        error_label = self.driver.find_element(*ForgotPasswordLocator.LABELERROR)
        return error_label.text