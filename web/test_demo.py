#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTestdemo():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_method(self, method):
        self.driver.quit()

    def test_testdemo(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.set_window_size(1421, 842)
        self.driver.find_element(By.LINK_TEXT, "所有分类").click()
        # 断言
        element = self.driver.find_element(By.LINK_TEXT, "所有分类")
        result = element.get_attribute("class")
        assert 'active' == result
