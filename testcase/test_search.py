from time import sleep

import yaml
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

    @pytest.mark.parametrize("name", yaml.safe_load(open("../testdata_yaml/test_search.yaml",encoding="utf-8")))
    def test_search(self,name):
        self.search.search(name)
        self.search.get_price(name)
