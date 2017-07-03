from Framework.basepageclass import BasePageClass
from Locators.AddEmployeePageLocators import AddEmployeePageLocator

class AddEmployeePage(BasePageClass):

    def add_employee_name(self,name):
        self.wait_for_element(30,*AddEmployeePageLocator.FIELDADDNAME1)
        name1 = self.driver.find_element(*AddEmployeePageLocator.FIELDADDNAME1)
        name1.send_keys(name)

    def add_employee_lastname(self,lastname):
        self.wait_for_element(30,*AddEmployeePageLocator.FIELDADDLASTNAME1)
        name1 = self.driver.find_element(*AddEmployeePageLocator.FIELDADDLASTNAME1)
        name1.send_keys(lastname)

    def add_employee_email(self,email):
        self.wait_for_element(30,*AddEmployeePageLocator.FIELDADDEMAIL1)
        name1 = self.driver.find_element(*AddEmployeePageLocator.FIELDADDEMAIL1)
        name1.send_keys(email)

    def add_employe_as(self,name,lastname,email):
        self.add_employee_name(name)
        self.add_employee_lastname(lastname)
        self.add_employee_email(email)

    def save_employees(self):
        btn_save = self.driver.find_element(*AddEmployeePageLocator.BTNSAVEEMPLOYEE)
        btn_save.click()

    def label_message(self):
        self.wait_for_text(30,*AddEmployeePageLocator.LABEL)
        label = self.driver.find_element(*AddEmployeePageLocator.LABEL)
        return label.text
