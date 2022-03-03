from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import pytest

class TestXueQiu:
    """
    改造1 pytest
    改造2 元素查找xpath
    改造3 将自动生成的find_element_by改造成find_element形式
    """
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        el1 = self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/tv_banner")
        el1.click()
        el2 = self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text")
        el2.send_keys("alibaba")
        el3 = self.driver.find_element(MobileBy.XPATH,"//*[@text='阿里巴巴']")
        el3.click()
        el4 = self.driver.find_element(MobileBy.XPATH,"//*[@text='加自选']")
        el4.click()

