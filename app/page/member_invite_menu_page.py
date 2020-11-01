#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
邀请页面
"""
from appium.webdriver.common.mobileby import MobileBy
# from app.page.contactadd_page import ContactAddPage
from app.page.base_page import BasePage


class MemberInviteMenuPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    def add_member_menual(self):
        # 点击【手动输入添加】
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()

        from app.page.contactadd_page import ContactAddPage
        return ContactAddPage(self.driver)

    def get_toast(self):
        result = self.get_toast_text()
        return result
