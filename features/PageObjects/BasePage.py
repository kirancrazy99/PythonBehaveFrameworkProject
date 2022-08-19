from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utilities import Configreader


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def entry(self, locator, value):
        self.driver.find_element(by=By.XPATH, value=Configreader.config_reader("locator", locator)).send_keys(value)

    def click(self, locator):
        self.driver.find_element(by=By.XPATH, value=Configreader.config_reader("locator", locator)).click()

    def select(self, locator, value):
        dropdown = self.driver.find_element(by=By.XPATH, value=Configreader.config_reader("locator", locator))
        select = Select(dropdown)
        select.select_by_visible_text(value)
