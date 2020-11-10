import yaml
from selenium.webdriver.common.by import By

from frame.base_page import BasePage
from frame.market import Market


class Main(BasePage):
    def goto_market(self):
        # 制造假的弹窗
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        # self.find(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        self.parse_yaml("./main.yaml", "goto_market")
        return Market(self.driver)
