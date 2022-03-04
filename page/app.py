from appium import webdriver

from page.base_page import BasePage
from page.main import Main


class App(BasePage):
    """
    inherit BasePage class
    """
    def start(self):
        """
        添加if else 判断；若不存在driver，添加driver参数，若driver存在，self._driver.launch_app()启动app
        :return: self实例，这样test case才能用串联模式：self.main = self.app.start().main()
        """
        if self._driver == None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps["noReset"] = True
            caps["unicodeKeyboard"] = True

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.launch_app()
        self._driver.implicitly_wait(10)

        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        """
        :return: Main类，类添加driver属性
        """
        return Main(self._driver)