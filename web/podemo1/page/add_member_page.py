#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AddMemberPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_member(self, username, account, phonenum):
        # 添加联系人
        sleep(2)
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(account)
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(phonenum)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        sleep(2)
        return True

    def get_member(self):
        # 验证联系人添加成功
        contactlist = self.driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        titlelist = [element.get_attribute("title") for element in contactlist]

        # titlelist = []
        # for element in contactlist:
        #     titlelist.append(element.get_attribute("title"))

        return titlelist
