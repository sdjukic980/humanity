from Framework.basictestcase import BaseTestCase
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Pages.StaffPage import StaffPage
from Pages.AddEmployeePage import AddEmployeePage
from Pages.AssignStaffPage import AssignStaffPage

class TestAddEmployee(BaseTestCase):

    def test_1_add_new_employee_as_manager(self):

        lp = LoginPage(self.driver)
        hp = HomePage(self.driver)
        sp = StaffPage(self.driver)
        ae = AddEmployeePage(self.driver)
        a_s = AssignStaffPage(self.driver)
        lp.login_as("sdjukic980@gmail.com","TestAutomationTask")
        hp.click_on_staff()
        sp.click_on_add_new_employee()
        ae.add_employe_as("Test","Employee1","test2@mycompany.com")
        ae.save_employees()
        self.assertEqual(ae.label_message(),"1 employees saved!")

    def test_2_add_existing_employee(self):

        lp = LoginPage(self.driver)
        hp = HomePage(self.driver)
        sp = StaffPage(self.driver)
        ae = AddEmployeePage(self.driver)
        a_s = AssignStaffPage(self.driver)
        lp.login_as("sdjukic980@gmail.com","TestAutomationTask")
        hp.click_on_staff()
        sp.click_on_add_new_employee()
        ae.add_employe_as("Test", "Employee1", "test2@mycompany.com")
        ae.save_employees()
        self.assertEqual(ae.label_message(),'0 employees saved!! But some emails already taken !')

    def test_3_add_employee_with_no_first_name(self):
        lp = LoginPage(self.driver)
        hp = HomePage(self.driver)
        sp = StaffPage(self.driver)
        ae = AddEmployeePage(self.driver)
        a_s = AssignStaffPage(self.driver)
        lp.login_as("sdjukic980@gmail.com", "TestAutomationTask")
        hp.click_on_staff()
        sp.click_on_add_new_employee()
        ae.add_employe_as("", "Employee1", "test2@mycompany.com")
        ae.save_employees()
        self.assertEqual(ae.label_message(), 'First Name cannot be left empty')





