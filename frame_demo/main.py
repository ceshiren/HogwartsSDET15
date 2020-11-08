from selenium.webdriver.common.by import By

from frame.base_page import BasePage
from frame.search import Search
from frame_demo.proxy import Proxy


class Main:
    def goto_search(self):
        Proxy(BasePage()).find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        return Search()
