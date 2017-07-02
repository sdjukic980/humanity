from Framework.basictestcase import BaseTestCase
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Locators.LoginPageLocators import LoginPageLocator


class TestLoginPage(BaseTestCase):

    def test_login_valid_credentals(self):
        lp = LoginPage(self.driver)
        lp.login_as("sdjukic980@gmail.com","TestAutomationTask")
        hp = HomePage(self.driver)
        self.assertTrue(hp.check_if_btn_schedule_present())

    def test_login_username_caps(self):
        lp = LoginPage(self.driver)
        lp.login_as("sdjukic980@gmail.com".capitalize(),"TestAutomationTask")
        self.assertTrue(lp.check_if_label_exists(*LoginPageLocator.LBLINCORRECT))

    def test_login_password_caps(self):
        lp = LoginPage(self.driver)
        lp.login_as("sdjukic980@gmail.com", "TestAutomationTask".capitalize())
        self.assertTrue(lp.check_if_label_exists(*LoginPageLocator.LBLINCORRECT))

    def test_login_username_missing(self):
        lp = LoginPage(self.driver)
        lp.login_as("","12345678")
        self.assertTrue(lp.check_if_label_exists(*LoginPageLocator.LBLVALIDMAIL))

    def test_login_password_missing(self):
        lp = LoginPage(self.driver)
        lp.login_as("sdjukic980@gmail.com","")
        self.assertTrue(lp.check_if_label_exists(*LoginPageLocator.LBLVALIDPASS))

    def test_login_username_and_pass_missing(self):
        lp = LoginPage(self.driver)
        lp.login_as("","")
        self.assertTrue(lp.check_if_label_exists(*LoginPageLocator.LBLVALIDMAIL))
        self.assertTrue(lp.check_if_label_exists(*LoginPageLocator.LBLVALIDPASS))


    def test_login_valid_user_invalid_pass(self):
        lp = LoginPage(self.driver)
        lp.login_as("sdjukic980@gmail.com","23456789")
        self.assertTrue(lp.check_if_label_exists(*LoginPageLocator.LBLINCORRECT))


    def test_login_invalid_user_valid_pass(self):
        lp = LoginPage(self.driver)
        lp.login_as("dummyuser","TestAutomationTask")
        self.assertTrue(lp.check_if_label_exists(*LoginPageLocator.LBLINCORRECT))