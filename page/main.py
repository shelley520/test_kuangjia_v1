from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage
from page.searchlist import SearchList


class Main(BasePage):

    def goto_search(self):
        """
        :return: Main类，类添加driver属性
        """
        el1 = self.find(MobileBy.ID, "com.xueqiu.android:id/tv_banner")
        el1.click()
        return SearchList(self._driver)