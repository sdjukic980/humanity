from selenium.webdriver.common.by import By

class AssignStaffLocator():

    EMPLOYEENAME = (By.XPATH,'//*[@id="_cd_staff"]/div[3]/table/tbody/tr/td[2]/div[2]/div/table/tbody/tr[5]/td[1]')
    MANAGERCHECKBOX = (By.XPATH,'//*[@id="_cd_staff"]/div[3]/table/tbody/tr/td[2]/div[2]/div/table/tbody/tr[7]/td[2]/label/input')
    POSSITIONSAVED = (By.XPATH,'//*[@id="_status"]')