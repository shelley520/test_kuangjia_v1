from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import pytest
from page.app import App

class TestXueQiu:

    def setup(self):
        """
        实例化app类
        获取self.app.start().main()
        """
        self.app = App()
        self.main = self.app.start().main()

    def test_search(self):
        self.main.goto_search().search("阿里巴巴-SW")
