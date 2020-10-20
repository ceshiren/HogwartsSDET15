#!/usr/bin/env python
# -*- coding: utf-8 -*-


def test_case1(cmdoption):
    env, datas = cmdoption
    ip = datas['env']['ip']
    port = datas['env']['port']
    url = str(ip) + ":" + str(port)
    print(url)
