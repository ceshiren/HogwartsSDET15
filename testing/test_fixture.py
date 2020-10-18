#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time


@pytest.mark.run(order=-1)
def test_case1(login):
    print(login)
    print("用例1")


# @pytest.mark.flaky(reruns=5, reruns_delay=2)
@pytest.mark.parametrize('a', [1, 2, 3])
@pytest.mark.first
def test_case2(a):
    # time.sleep(2)
    assert False
    print("用例2")


@pytest.mark.run(order=2)
def test_case3(conn_db):
    print(conn_db)
    print("用例3")


@pytest.mark.run(order=4)
def test_case4():
    assert True
    assert False
    assert 1 == 2


@pytest.mark.parametrize(('x', 'y'), [(1, 1), (1, 0), (0, 1)])
@pytest.mark.run(order=3)
def test_simple_assume(x, y):
    pytest.assume(x == y)
    pytest.assume(True)
    pytest.assume(False)
