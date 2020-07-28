from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config import Config
class MailSignIn():
    provider_link = ''
    provider_email = ''
    provider_password = ''
    provider_email_xpath =''
    provider_password_xpath = ''
    provider_login_xpath = ''
    provider_login_btn = ''

    def __init__(self, provider):
        self.provider_link = provider['login_url']
        self.provider_email = provider['email']
        self.provider_password = provider['password']
        self.provider_email_xpath = provider['email_xpath']
        self.provider_password_xpath = provider['passwd_xpath']
        self.provider_login_xpath = provider['login_xpath']
        self.provider_login_btn = provider['login_btn']

    def validate_login(self):
        try:
            cfg = Config()
            driver = cfg.get_selenium_driver()
            driver.get(self.provider_link)
            driver.find_element_by_xpath(self.provider_email_xpath).send_keys(self.provider_email)
            driver.find_element_by_xpath(self.provider_login_xpath).click()
            element_present = EC.presence_of_element_located((By.XPATH, self.provider_password_xpath))
            WebDriverWait(driver, 3).until(element_present)
            driver.find_element_by_xpath(self.provider_password_xpath).send_keys(self.provider_password)
            driver.find_element_by_xpath(self.provider_login_btn).click()
        except TimeoutException:
            print("Loading took too much time!")

if __name__=="__main__":
    cfg = Config()
    provider_config = cfg.get_config_prop('yahoo')
    mail_sign_in = MailSignIn(provider_config)
    mail_sign_in.validate_login()