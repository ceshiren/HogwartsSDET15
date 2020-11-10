from selenium.webdriver.common.by import By

from frame.base_page import BasePage


class Search(BasePage):
    def search(self):
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("alibaba")
        self.parse_yaml("./search.yaml", "search")