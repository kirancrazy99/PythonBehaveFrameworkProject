from Utilities.Configreader import config_reader
from features.PageObjects.BasePage import BasePage


class RegistrationPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def open(self,url):
        self.driver.get(url)

    def setName(self,name):
        self.driver.entry(config_reader("name_Xpath"),name)

    def setphoneNum(self,phoneNum):
        self.driver.entry(config_reader("name_Xpath"),phoneNum)

    def setemail(self,email):
        self.driver.entry(config_reader("name_Xpath"),email)

    def setcity(self,city):
        self.driver.entry(config_reader("name_Xpath"),city)

    def setcountry(self,country):
        self.driver.select(config_reader("name_Xpath"),country)

    def setusername(self,username):
        self.driver.entry(config_reader("name_Xpath"),username)

    def setpassword(self,password):
        self.driver.entry(config_reader("name_Xpath"),password)

    def submit(self):
        self.driver.click(config_reader("name_Xpath"))