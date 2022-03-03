from appium.webdriver.common.mobileby import MobileBy

from page.searchlist import SearchList


class Main:
    def __init__(self,driver):
        self._driver = driver

    def goto_search(self):
        el1 = self._driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_banner")
        el1.click()
        return SearchList(self._driver)