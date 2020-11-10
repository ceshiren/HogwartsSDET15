from selenium.webdriver.common.by import By

from frame.base_page import BasePage
from frame_demo.proxy import Proxy


class Search:
    def search(self):
        Proxy(BasePage()).find(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()