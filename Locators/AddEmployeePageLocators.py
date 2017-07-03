from selenium.webdriver.common.by import By

class AddEmployeePageLocator:

    FIELDADDNAME1 = (By.XPATH,'//*[@id="_asf1"]')
    FIELDADDLASTNAME1 = (By.XPATH,'//*[@id="_asl1"]')
    FIELDADDEMAIL1 = (By.XPATH,'//*[@id="_ase1"]')
    BTNSAVEEMPLOYEE = (By.XPATH,'//*[@id="_as_save_multiple"]')
    LABEL = (By.XPATH,'//*[@id="_status"]')