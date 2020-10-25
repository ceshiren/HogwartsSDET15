#!/usr/bin/env python
# -*- coding: utf-8 -*-
from web.podemo1.page.main_page import MainPage


class TestWX:
    def setup(self):
        self.main = MainPage()

    def test_addmember(self):
        username = "aaaaaac"
        account = "aaaaaac_hogwarts"
        phonenum = "13400000002"

        addmember = self.main.goto_addmember()
        addmember.add_member(username, account, phonenum)
        assert username in addmember.get_member()
