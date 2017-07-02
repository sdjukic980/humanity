from Framework.basepageclass import BasePageClass
from Locators.HomePageLocators import HomePageLocator

class HomePage(BasePageClass):

    def check_if_btn_schedule_present(self):
        self.wait_for_element(30,*HomePageLocator.BTNSCHEDULE)
        btn_schedule = self.driver.find_element(*HomePageLocator.BTNSCHEDULE)
        return btn_schedule

    def click_on_contacts(self):
        self.wait_for_element(30,*HomePageLocator.CONTACTS)
        contact = self.driver.find_element(*HomePageLocator.CONTACTS)
        contact.click()