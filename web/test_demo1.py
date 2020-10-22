#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestTestdemo():
    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()

    def teardown_method(self, method):
        self.driver.quit()

    def test_testdemo(self):
        self.driver.get("http://www.baidu.com")
        sleep(3)

    def test_weixin(self):
        self.driver.find_element(By.ID, "menu_contacts").click()
        sleep(3)

    def test_cookie(self):
        # get_cookies() 可以获取当前打开的页面的cookies 信息
        # add_cookie() 可以把cookie 添加到当前的页面中去
        # cookies = self.driver.get_cookies()
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851905935585'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851905935585'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325054155915'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'IiwmHmbRQC3UgqmekvGcstL98cguenn0rw3oSVFLMdYC5HxRMiD_9oqIuKwP_A4x'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a8796034'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '4265340051991539'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1603401527, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '1c9etn1'},
            {'domain': '.qq.com', 'expiry': 1603457502, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.15599625.1603101807'},
            {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'ycykxRqS4P'},
            {'domain': '.qq.com', 'expiry': 1605668087, 'httpOnly': False, 'name': 'lskey', 'path': '/',
             'secure': False,
             'value': '00010000fdcb43941d5ee20cf2e16bd1e33bc5c0500e95b36058fd986fb08c77642fbd12fb15c939a1bb8468'},
            {'domain': '.qq.com', 'expiry': 1915084825, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': False, 'value': '1_2163046706'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '6944625664'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1605963112, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'en'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': '75461a3126cbb39ff08f9bd58fe42c2d3b5c887a4e78ca4031e34ead02c3c44c'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/',
             'secure': False, 'value': '2163046706'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'expiry': 1634725751, 'httpOnly': False,
                                  'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                                  'value': '1603101806,1603188257,1603189751'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '8205526055'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'ta1pVuy2AlGFOV2HgP_NbxGv6yczHyjTS_y068H5SqaaNAURledi8-CDqit7LKsfYNYBbmAHbrDkIgNoA3TgDnPznpIks9e440Soc59mKuAnpXY0epMc8JhG_KwJy0P2vvjUe7_58j6_pQSyUodztQLKmwuC9TdpowSup5lxGf3R2FfpTTO9yNoVwNaYQIlnjBxonIF4ICPA8ohML_phggViW51GBnVc1JZL7fzKJTS04uwzN2S7seiD3jk30CPcmrYzIulvDzXRrJxuVlcBBA'},
            {'domain': '.qq.com', 'expiry': 1605668087, 'httpOnly': False, 'name': 'luin', 'path': '/', 'secure': False,
             'value': 'o2163046706'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1634637786, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 1666443102, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1737553657.1582007476'}]

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)

    def test_shelve(self):
        # shelve python 内置模块，专门用来对数据进行持久化存储的库，相当于小型的数据库
        # 可以通过 key，value 来把数据保存到shelve中
        # 读取cookie
        db = shelve.open("cookies")
        cookies = db['cookie']
        db.close()
        # 利用读取的cookie 完成登录操作
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        # 找到"导入联系人"按钮
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        # 上传
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys(
            "/Users/juanxu/Downloads/mydata.xlsx")
        # 验证 上传文件名
        filename = self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text
        assert "mydata.xlsx" == filename
        sleep(3)
