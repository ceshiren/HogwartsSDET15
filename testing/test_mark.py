#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.mark.login
def test_login1():
    print("登录用例")


@pytest.mark.login
def test_login2():
    print("登录用例2")


@pytest.mark.search
def test_search1():
    print("搜索用例")


@pytest.mark.search
def test_search2():
    print("搜索用例")
