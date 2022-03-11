from time import sleep
from selenium.webdriver.common.by import By
import yaml
from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage


class SearchList(BasePage):

    def search(self,name):
        self._params["name"] = name
        self.steps("../teststep_yaml/searchlist.yaml")

    def get_price(self,name):
        self._params["name"] = name
        print(self.steps("../teststep_yaml/searchlist.yaml"))
