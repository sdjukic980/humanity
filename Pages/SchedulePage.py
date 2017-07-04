from Framework.basepageclass import BasePageClass
from Locators.ScheduleLocators import ScheduleLocator

class SchedulePage(BasePageClass):

    def search_for_employee(self,employee):
        self.wait_for_element(*ScheduleLocator.SEARCHBAR)
        search_bar = self.driver.find_element(*ScheduleLocator.SEARCHBAR)
        search_bar.send_keys(employee)

    def enter_schedule_for_day(self,time,*day):
        self.wait_for_element(day[0],day[1])
        day = self.driver.find_element(day[0],day[1])
        day.click()
        enter_time = self.driver.find_element(*ScheduleLocator.ENTERTIME)
        enter_time.send_keys(time)
