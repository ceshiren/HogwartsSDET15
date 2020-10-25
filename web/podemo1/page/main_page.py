#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from web.podemo1.page.add_member_page import AddMemberPage
from web.podemo1.page.base_page import BasePage


class MainPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    # def __init__(self):
    #     options = Options()
    #     options.debugger_address = "127.0.0.1:9222"
    #     self.driver = webdriver.Chrome(options=options)
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    # 添加联系人
    def goto_addmember(self):
        # click addmember
        # 直接在首页点击【添加联系人】
        # self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()

        # 点击 【联系人】
        self.driver.find_element(By.CSS_SELECTOR, "#menu_contacts").click()
        sleep(2)
        # 点击 【添加联系人】按钮
        self.driver.find_element(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)").click()

        return AddMemberPage(self.driver)
