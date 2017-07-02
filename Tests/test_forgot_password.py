from Framework.basictestcase import BaseTestCase
from Pages.LoginPage import LoginPage
from Pages.ForgotPasswordPage import ForgotPasswordPage
from Locators.ForgotPasswordLocators import ForgotPasswordLocator
from Locators.LoginPageLocators import LoginPageLocator
from time import sleep


class TestForgotPassword(BaseTestCase):

    def test_forgot_pass_page(self):
        lp = LoginPage(self.driver)
        lp.click_forgot_password()
        self.assertTrue(lp.check_if_element_exists(*ForgotPasswordLocator.RESETPASSTEXT))

    def test_forgot_pass_back_to_login(self):
        lp = LoginPage(self.driver)
        lp.click_forgot_password()
        fp = ForgotPasswordPage(self.driver)
        fp.click_back_to_login()
        self.assertTrue(lp.check_if_element_exists(*LoginPageLocator.WELCOME))

    def test_forgot_pass_invalid_mail(self):
        lp = LoginPage(self.driver)
        lp.click_forgot_password()
        fp = ForgotPasswordPage(self.driver)
        fp.enter_email("test")
        fp.click_request_new_pass_btn()
        fp.wait_for_element(30,*ForgotPasswordLocator.LBLEMAILISREQUIRED)
        self.assertTrue(fp.check_if_element_exists(*ForgotPasswordLocator.LBLEMAILISREQUIRED))

    def test_forgot_pass_incorrect_mail(self):
        lp = LoginPage(self.driver)
        lp.click_forgot_password()
        fp = ForgotPasswordPage(self.driver)
        fp.enter_email("testuser@test.gov")
        fp.click_request_new_pass_btn()
        self.assertTrue(fp.check_if_element_exists(*ForgotPasswordLocator.LBLEMAILISREQUIRED))