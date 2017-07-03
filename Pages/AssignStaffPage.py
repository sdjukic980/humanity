from Framework.basepageclass import BasePageClass
from Locators.AssignStaffLocators import AssignStaffLocator

class AssignStaffPage(BasePageClass):

    def check_role(self):
        self.wait_for_element(30,*AssignStaffLocator.MANAGERCHECKBOX)
        chckbox = self.driver.find_element(*AssignStaffLocator.MANAGERCHECKBOX)
        chckbox.click()

    def possition_saved(self):
        self.wait_for_element(30,*AssignStaffLocator.POSSITIONSAVED)
        label = self.driver.find_element(*AssignStaffLocator.POSSITIONSAVED)
        return label.text