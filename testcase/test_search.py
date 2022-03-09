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
        self.search = App().start().main().goto_search()

    def test_search(self):
        self.search.search()
        self.search.get_price()
