import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.searchlist import SearchList


class Main(BasePage):

    def goto_search(self):
        """
        :return: Main类，类添加driver属性
        """
        # //*[@resource-id = 'yeye元素']//*[@text='孙子元素']
        # self.find(By.ID, "com.xueqiu.android:id/tv_banner").click()
        self.steps("../page/main.yaml","main")
        return SearchList(self._driver)