#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 被测代码 ，计算器（加 减 乘 除）
class Calculator:
    def add(self, a, b):
        return a + b

    def add1(self, a: int, b: int) -> int:
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b
