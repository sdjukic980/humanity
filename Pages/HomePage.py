from Framework.basepageclass import BasePageClass
from Locators.HomePageLocators import HomePageLocator

class HomePage(BasePageClass):

    def check_if_btn_schedule_present(self):
        self.wait_for_element(30,*HomePageLocator.BTNSCHEDULE)
        btn_schedule = self.driver.find_element(*HomePageLocator.BTNSCHEDULE)
        return btn_schedule

    def click_on_staff(self):
        self.wait_for_element(30,*HomePageLocator.BTNSTAFF)
        btn_staff = self.driver.find_element(*HomePageLocator.BTNSTAFF)
        btn_staff.click()