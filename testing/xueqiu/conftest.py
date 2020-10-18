#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture()
def conn_db():
    print("完成 数据库连接aaaaaa")
    yield "database"
    print("关闭 数据库连接aaaaaa")
