from Framework.basictestcase import BaseTestCase
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Pages.SchedulePage import SchedulePage
from Locators.ScheduleLocators import ScheduleLocator

class TestAddSchedule(BaseTestCase):

    def test_add_schedule(self):
        lp = LoginPage(self.driver)
        hp = HomePage(self.driver)
        sp = SchedulePage(self.driver)
        lp.login_as("sdjukic980@gmail.com","TestAutomationTask")
        hp.click_on_schedule()
        sp.search_for_employee("Test Employee1\n")
        sp.enter_schedule_for_day("08:00-15:00\n",*ScheduleLocator.DAY1)
        sp.driver.refresh()
        sp.search_for_employee("Test Employee1\n")


