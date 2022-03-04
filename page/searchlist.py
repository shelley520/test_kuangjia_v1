from time import sleep
from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage


class SearchList(BasePage):

    def search(self,name):
    # 输入查询文字
        el2 = self.find(MobileBy.ID,"com.xueqiu.android:id/search_input_text")
        el2.send_keys(name)
        #点击查询结果
        el3 = self.find(MobileBy.XPATH,f"//*[@resource-id='com.xueqiu.android:id/name' and @text='{name}']")
        el3.click()
        #获取股票价格
        el4 = self.find(MobileBy.XPATH,f"//*[@text='{name}']/../..//*[@resource-id='com.xueqiu.android:id/price_layout']/*[@class='android.widget.TextView'][1]").text
        print(el4)
        sleep(5)