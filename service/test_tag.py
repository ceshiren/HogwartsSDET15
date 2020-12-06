import datetime

import pytest
# done: 与底层具体的实现框架代码耦合严重，无法适应变化，比如公司切换了协议，比如使用pb dubbo
# done: 代码冗余，需要封装
# done: 无法清晰的描述业务
# done: 使用jsonpath表达更灵活的递归查找
from jsonpath import jsonpath
from service.tag import Tag


class TestTag:
    def setup_class(self):
        self.tag = Tag()

    @pytest.mark.parametrize("tag_id, tag_name", [
        ['et_6ElDwAAK8oJuAJ82drAyVi7DBhJyA', 'tag1_new_'],
        ['et_6ElDwAAxqiLMGOboky3_SyekzNUuA', 'tag1——中文'],
        ['et_6ElDwAA3p5Mmu7lR_C2S4s2Pw571w', 'tag1[中文]'],
    ])
    def test_tag_list(self, tag_id, tag_name):
        tag_name = tag_name + str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        r = self.tag.list()
        r = self.tag.update(
            id=tag_id,
            tag_name=tag_name
        )
        r = self.tag.list()
        # tags = [
        #     tag2

        #     for group in r.json()['tag_group'] if group['group_name'] == group_name
        #     for tag in group['tag'] if tag['name'] == tag_name
        # ]

        assert jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['name'] == tag_name
        # assert tags != []

    def test_list(self):
        self.tag.list()

    # 如果 40071 ，UserTag Name Already Exist
    # 1. 删除对应 tag （推荐）
    # 2. 已有 tag_name 的基础上，追加名字（时间戳，计数器）
    def test_add_tag(self):
        # todo: 测试数据要放到数据文件中
        group_name = "TMP00123"
        tag = [
            {"name": "TAG3"},
            {"name": "TAG2"},
            {"name": "TAG3"},
        ]

        r = self.tag.add(group_name=group_name, tag=tag)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

    def test_add_and_detect(self):
        group_name = "TMP00123"
        tag = [
            {"name": "TAG1"},
            {"name": "TAG2"},
            {"name": "TAG3"},
        ]
        r = self.tag.add_and_detect(group_name, tag)
        assert r

    # 如果 40068 ，invalid tagid
    # 0. 添加 tag
    # 1. 删除 tag 有问题
    # 2. 再进行重试（重试次数： n）：手动实现，借助 pytest 钩子（rerun插件）
    #   a. 添加一个接口
    #   b. 对新添加的接口再删除
    #   c. 查询删除是否成功
    def test_delete_group(self):
        self.tag.delete_group(["et_6ElDwAAzdH3nsV5g24aSO4ZUQyBOg"])

    def test_delete_tag(self):
        self.tag.delete_tag(["et_6ElDwAAgItYmM3RQYkH3dhdAI8_QA"])

    def test_delete_and_detect_group(self):
        r = self.tag.delete_and_detect_group(["et_6ElDwAAyvuY_HFzh0vHvy-yqYhVHA"])
        assert r.json()["errcode"] == 0
