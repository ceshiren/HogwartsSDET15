#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.page.app import App


class TestContact:

    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    def test_addcontact(self):
        name = "hogwarts__004"
        gender = "男"
        phonenum = "13500000003"

        result = self.main.goto_address() \
            .click_addmember(). \
            add_member_menual(). \
            add_contact(name, gender, phonenum).get_toast()
        assert '添加成功' == result
