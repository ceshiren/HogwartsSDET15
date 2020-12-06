import datetime
import json

import requests

from service.base_api import BaseApi


class Tag(BaseApi):

    def __init__(self):
        super().__init__()

    def find_group_id_by_name(self, group_name):
        # 查询元素是否存在，如果不存在，报错
        for group in self.list().json()["tag_group"]:
            if group_name in group["group_name"]:
                return group["group_id"]
        print("group name not in goup")
        return ""

    def is_group_id_exist(self, group_id):
        # 查询元素是否存在，如果不存在，报错
        for group in self.list().json()["tag_group"]:
            if group_id in group["group_id"]:
                return True
        print("group id not in goup")
        return False

    def add(self, group_name, tag, **kwargs):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            "params": {"access_token": self.token},
            "json": {"group_name": group_name,
                     "tag": tag,
                     **kwargs
                     }}
        return self.send(data)

    # step 1  => step1 false
    # step 2  => step2 true
    # step 3  => step3 true
    def add_and_detect(self, group_name, tag, **kwargs):
        r = self.add(group_name, tag, **kwargs)
        # 如果删除的元素已经存在地
        if r.json()["errcode"] == 40071:
            group_id = self.find_group_id_by_name(group_name)
            if not group_id:
                # 元素不在，接口有问题
                return ""
            self.delete_group([group_id])
            self.add(group_name, tag, **kwargs)
        result = self.find_group_id_by_name(group_name)
        if not result:
            print("add not success")
        return result

    def list(self):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            "params": {"access_token": self.token},
            "json": {'tag_id': []}}
        r = self.send(data)
        return r

    def update(self, id, tag_name):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
            "params": {"access_token": self.token},
            "json": {
                'id': id,
                'name': tag_name
            }}
        r = self.send(data)
        return r

    # 查询 tag_id ->  删除 tag_id
    # 如果正常： 成功
    # {
    #     "errcode": 0,
    #     "errmsg": "ok"
    # }
    # 如果异常： 失败（）
    # 　手动获取

    def delete_group(self, group_id):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params": {"access_token": self.token},
            "json": {
                "group_id": group_id
                # "tag_id": ["et_6ElDwAA6RQb_EVpMei30pmbsy-Zpw"],
            }}
        r = self.send(data)
        return r

    def delete_tag(self, tag_id):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params": {"access_token": self.token},
            "json": {
                "tag_id": tag_id
            }}
        r = self.send(data)
        return r

    def delete_and_detect_group(self, group_ids):
        deleted_group_ids = []
        r = self.delete_group(group_ids)
        if r.json()["errcode"] == 40068:
            # 如果标签不存在，就添加一个标签，将它的 group_id 存储进来
            for group_id in group_ids:
                if not self.is_group_id_exist(group_id):
                    group_id_tmp = self.add_and_detect(group_name="TMP00123",
                                                       tag=[{"name": "TAG1"}])
                    deleted_group_ids.append(group_id_tmp)
                # 如果标签存在，就将它存入标签组
                else:
                    deleted_group_ids.append(group_id)
            r = self.delete_group(deleted_group_ids)
        return r
