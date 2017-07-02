from selenium.webdriver.common.by import By

class ForgotPasswordLocator():

    RESETPASSTEXT = (By.XPATH,'//*[@id="request_reset_password"]/h1')
    RETURNTOLOGIN = (By.XPATH,'//*[@id="request_reset_password"]/div[1]/a')
    ENTEREMAIL = (By.XPATH,'//*[@id="email"]')
    BTNREQUESTNEWPASSWORD = (By.XPATH,'//*[@id="request_reset_password"]/div[4]/button')
    LBLEMAILISREQUIRED = (By.XPATH,'//*[@id="error"]')
