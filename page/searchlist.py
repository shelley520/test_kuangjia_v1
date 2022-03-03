from time import sleep

from appium.webdriver.common.mobileby import MobileBy


class SearchList:
    def __init__(self,driver):
        self._driver = driver

    def search(self):
    # 输入查询文字
        el2 = self._driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text")
        el2.send_keys("阿里巴巴")
        #点击查询结果
        el3 = self._driver.find_element(MobileBy.XPATH,"//*[@text='阿里巴巴']")
        el3.click()
        #获取股票价格
        el4 = self._driver.find_element(MobileBy.XPATH,"//*[@text='阿里巴巴']/../..//*[@resource-id='com.xueqiu.android:id/price_layout']/*[@class='android.widget.TextView'][1]").text
        print(el4)
        sleep(5)