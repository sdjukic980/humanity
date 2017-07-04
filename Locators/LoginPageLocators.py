from selenium.webdriver.common.by import By

class LoginPageLocator:

    USERNAME = (By.XPATH,'//*[@id="email"]')
    PASSWORD = (By.XPATH,'//*[@id="password"]')
    BTNLOGIN = (By.XPATH,'//*[@id="LoginForm"]/div[3]/div/button')
    LBLINCORRECT = (By.XPATH,'//*[@id="incorrect"]')
    LBLVALIDMAIL = (By.XPATH,'//*[@id="valid_email"]')
    LBLVALIDPASS = (By.XPATH,'//*[@id="valid_password"]')
    FORGOTPASSWORD = (By.XPATH,'//*[@id="login"]/div[2]/div[2]/a')
    WELCOME = (By.XPATH,'//*[@id="hum-banner"]/p')
    LBLNOTACTIVATED = (By.XPATH,'//*[@id="notactivated"]')
    LBLACCOUNTNOTACTIVATED = (By.XPATH,'//*[@id="notactivated"]')

