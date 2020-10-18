#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

import pytest

from pythoncode.calculator import Calculator


@pytest.fixture(scope='session', autouse=True)
def conn_db():
    print("完成 数据库连接")
    yield "database"
    print("关闭 数据库连接")


@pytest.fixture(scope="function", params=['tom', 'jerry'])
def login(request):
    # setup 操作
    print("登录操作")
    username = request.param
    # yield 相当于return 操作
    yield username
    # teardown操作
    print("登出操作")


@pytest.fixture(scope="class")
def get_calc():
    print("计算开始")
    calc = Calculator()
    yield calc
    print("计算结束")


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(type(items))
    items.reverse()

    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        if 'add' in item._nodeid:
            item.add_marker(pytest.mark.add)
        elif 'div' in item._nodeid:
            item.add_marker(pytest.mark.div)
