#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


@pytest.mark.parametrize('c', [7, 8, 9])
@pytest.mark.parametrize('b', [4, 5, 6])
@pytest.mark.parametrize('a', [1, 2, 3])
def test_parm(a, b, c):
    print(a, b, c)
