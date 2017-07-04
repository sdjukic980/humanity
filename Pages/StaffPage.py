from Framework.basepageclass import BasePageClass
from Locators.StaffPageLocators import StaffPageLocator

class StaffPage(BasePageClass):

    def click_on_add_new_employee(self):
        self.wait_for_element(*StaffPageLocator.BTNADDEMPLOYEE)
        btn_add_employee = self.driver.find_element(*StaffPageLocator.BTNADDEMPLOYEE)
        btn_add_employee.click()
