#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 通讯录界面
from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage
from app.page.member_invite_menu_page import MemberInviteMenuPage


class AddressListPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def click_addmember(self):
        # 滚动查找【添加成员】
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()\
        #                          .scrollable(true).instance(0))\
        #                          .scrollIntoView(new UiSelector()\
        #                          .text("添加成员").instance(0));').click()
        self.find_by_scroll("添加成员").click()

        return MemberInviteMenuPage(self.driver)
