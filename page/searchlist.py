from time import sleep
from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage


class SearchList(BasePage):

    def search(self):
    # 输入查询文字
        el2 = self.find(MobileBy.ID,"com.xueqiu.android:id/search_input_text")
        el2.send_keys("阿里巴巴")
        #点击查询结果
        el3 = self.find(MobileBy.XPATH,"//*[@text='阿里巴巴']")
        el3.click()
        #获取股票价格
        el4 = self.find(MobileBy.XPATH,"//*[@text='阿里巴巴']/../..//*[@resource-id='com.xueqiu.android:id/price_layout']/*[@class='android.widget.TextView'][1]").text
        print(el4)
        sleep(5)