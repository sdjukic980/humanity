from Framework.basictestcase import BaseTestCase
from Pages.LoginPage import LoginPage
from Pages.ForgotPasswordPage import ForgotPasswordPage
from Locators.ForgotPasswordLocators import ForgotPasswordLocator
from Locators.LoginPageLocators import LoginPageLocator


class TestForgotPassword(BaseTestCase):

    def test_forgot_pass_page(self):
        lp = LoginPage(self.driver)
        fp = ForgotPasswordPage(self.driver)
        lp.click_forgot_password()
        self.assertEqual(fp.element_text(*ForgotPasswordLocator.RESETPASSTEXT),'Reset password')


    def test_forgot_pass_back_to_login(self):
        lp = LoginPage(self.driver)
        lp.click_forgot_password()
        fp = ForgotPasswordPage(self.driver)
        fp.click_back_to_login()
        self.assertEqual(fp.element_text(*LoginPageLocator.WELCOME),'Welcome to your new Humanity login page')

    def test_forgot_pass_invalid_mail(self):
        lp = LoginPage(self.driver)
        lp.click_forgot_password()
        fp = ForgotPasswordPage(self.driver)
        fp.enter_email("test")
        fp.click_request_new_pass_btn()
        self.assertEqual(fp.element_text(*ForgotPasswordLocator.LABELERROR),'Not valid e-mail address')

    def test_forgot_pass_incorrect_mail(self):
        lp = LoginPage(self.driver)
        lp.click_forgot_password()
        fp = ForgotPasswordPage(self.driver)
        fp.enter_email("testuser@test.gov")
        fp.click_request_new_pass_btn()
        self.assertEqual(fp.element_text(*ForgotPasswordLocator.LABELERROR),'Invalid user')
