import yaml
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from frame.hand_black import handle_black


class BasePage:
    black_list = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]
    max_num = 3
    error_num = 0

    def __init__(self, driver: WebDriver = None):
        """
        初始化应用
        """
        if driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps["noReset"] = "true"
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

    @handle_black
    def find(self, by, locator=None):
        """
        查找元素
        :return:
        """

        if locator is None:
            # 如果传的元素是一个，只有 by
            result = self.driver.find_element(*by)
        else:
            # 如果传的元素是二个，既有 by ，又有 locator
            result = self.driver.find_element(by, locator)
        return result

    def parse_yaml(self, path, func_name):
        """
        读取 yaml ，取出关键数据，用 parse 进行解析
        :param path:
        :param func_name:
        :return:
        """
        with open(path, encoding="utf-8") as f:
            data = yaml.load(f)
        self.parse(data[func_name])

    def parse(self, steps):
        """
        解析 yaml　内容
        :param steps:
        :return:
        """
        # 遍历每一个步骤
        for step in steps:
            # 如果是点击
            if 'click' == step['action']:
                self.find(step['by'], step['locator']).click()
            # 如果是发送内容
            elif 'send' == step['action']:
                self.find(step['by'], step['locator']).send_keys(step["content"])
