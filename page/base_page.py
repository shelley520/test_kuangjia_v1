from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from page.wrapper import handle_black


class BasePage:
    """
    create BasePage class due to there is same __init__ function in each class
    create init function in BasePage, and let the other class inherit the BasePage class
    """


    def __init__(self,driver:WebDriver = None):
        self._driver = driver
    @handle_black
    def finds(self,locator,value:str=None):
        element: list
        if isinstance(locator,tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator,value)
        return elements

    @handle_black
    def find(self,locator,value:str = None):
        element: WebDriver
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        return element
