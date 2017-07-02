from Framework.basictestcase import BaseTestCase
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Pages.StaffPage import StaffPage

class TestAddEmployee(BaseTestCase):

    def test_add_new_employee_as_manager(self):
        lp = LoginPage(self.driver)
        hp = HomePage(self.driver)
        sp = StaffPage(self.driver)
        lp.login_as("sdjukic980@gmail.com","TestAutomationTask")
        hp.click_on_staff()
        sp.click_on_add_new_employee()
