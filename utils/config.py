import configparser
from selenium import webdriver
class Config():
    def get_config_prop(self, section_name):
        try:
            config = configparser.ConfigParser()
            config.read('./config/config.properties')
            section_data = dict(config.items(section_name))
            provider = self.providers()
            provider["email"]=config[section_name][section_name+".email"]
            provider["password"] = config[section_name][section_name + ".password"]
            provider["login_url"] = config[section_name][section_name + ".loginurl"]
            provider["email_xpath"] = config[section_name][section_name + ".name_xpath"]
            provider["passwd_xpath"] = config[section_name][section_name + ".pwd_xpath"]
            provider["login_xpath"] = config[section_name][section_name + ".next_xpath"]
            provider["login_btn"] = config[section_name][section_name + ".login_button_xpath"]
            return provider
        except:
            print("No Section found",section_name)

    def get_selenium_driver(self):
        DRIVER_PATH = './chromedriver'
        driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        return driver

    def providers(self):
        return {'email': '', 'password': '', 'login_url': '','email_xpath':'','passwd_xpath':'','login_xpath':'','login_btn':''}
