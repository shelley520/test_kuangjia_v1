from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

def handle_black(func):
    def wrapper(*args,**kwargs):
        from page.base_page import BasePage
        _black_list = [
            (By.XPATH, "//*[@text='确认']")
        ]
        _max_num = 3
        _error_num = 0
        isinstance:BasePage = args[0]
        try:
            element = func(*args,**kwargs)
            _error_num = 0
            isinstance._driver.implicitly_wait(5)
            return element
        except Exception as e:
            isinstance._driver.implicitly_wait(1)
            if _error_num > _max_num:
                raise e
            _error_num += 1
            for ele in _black_list:
                elelist = isinstance._driver.find_elements(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    return wrapper(*args, **kwargs)
            raise e
    return wrapper